from fifa_rating.entity.config_entity import DataIngestionConfig
from fifa_rating.exception import FifaException
from fifa_rating.logger import logging
from fifa_rating.entity.artifact_entity import DataIngestionArtifact
from six.moves import urllib
from sklearn.model_selection import StratifiedShuffleSplit
import pandas as pd
import numpy as np
import sys
import os
import zipfile
import sqlite3


class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig) -> None:
        try:
            logging.info(f"{'='*20}Data Ingestion log started.{'='*20}")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise FifaException(e,sys)

    def download_fifa_data(self,):
        try:

            download_url = self.data_ingestion_config.dataset_download_url
            
            zip_download_dir = self.data_ingestion_config.zip_download_dir
            
            if os.path.exists(zip_download_dir):
                os.remove(zip_download_dir)

            os.makedirs(zip_download_dir,exist_ok=True)

            sqlite_file_name = 'archive.zip'

            zip_file_path = os.path.join(zip_download_dir,sqlite_file_name)

            logging.info(f"Downloading file from :[{download_url}] into:[{zip_file_path}]")
            urllib.request.urlretrieve(download_url, zip_file_path)

            logging.info(f"File: [{zip_file_path}] has been downloaded successfully.")
            return zip_file_path
        
        except Exception as e:
            raise FifaException(e,sys) from e

    def extract_zip_file(self,zip_file_path:str):
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)

            os.makedirs(raw_data_dir,exist_ok=True)

            logging.info(f"Extracting zip file: [{zip_file_path}] into dir: [{raw_data_dir}]")
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(raw_data_dir)
            logging.info(f"Extraction completed")

        except Exception as e:
            raise FifaException(e,sys) from e
    
    def split_data_as_train_test(self) -> DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            file_name = os.listdir(raw_data_dir)[0]

            fifa_file_path = os.path.join(raw_data_dir,file_name)

            
            logging.info(f"Connecting to SQL database: [{fifa_file_path}]")
            cnx = sqlite3.connect(fifa_file_path)
            fifa_data_frame = pd.read_sql_query("SELECT * FROM Player_Attributes", cnx)

            logging.info(f"Reading csv file: [{fifa_file_path}]")

            fifa_data_frame = fifa_data_frame.dropna(subset=['overall_rating'])

            fifa_data_frame["rating_cat"] = pd.cut(
                fifa_data_frame["overall_rating"],
                bins=[30.0,40.0,50.0,60.0,70.0,80.0,90.0,np.inf],
                labels=['<40','<50','<60','<70','<80','<90','<100']
            )
            

            logging.info(f"Splitting data into train and test")
            strat_train_set = None
            strat_test_set = None

            split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

            for train_index,test_index in split.split(fifa_data_frame, fifa_data_frame["overall_rating"]):
                strat_train_set = fifa_data_frame.iloc[train_index].drop(["overall_rating"],axis=1)
                strat_test_set = fifa_data_frame.iloc[test_index].drop(["overall_rating"],axis=1)

            file_name="data.csv"

            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir,
                                            file_name)

            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir,
                                        file_name)
            
            if strat_train_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir,exist_ok=True)
                logging.info(f"Exporting training datset to file: [{train_file_path}]")
                strat_train_set.to_csv(train_file_path,index=False)

            if strat_test_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir, exist_ok= True)
                logging.info(f"Exporting test dataset to file: [{test_file_path}]")
                strat_test_set.to_csv(test_file_path,index=False)
            

            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
                                test_file_path=test_file_path,
                                is_ingested=True,
                                message=f"Data ingestion completed successfully."
                                )
            logging.info(f"Data Ingestion artifact:[{data_ingestion_artifact}]")
            return data_ingestion_artifact

        except Exception as e:
            raise FifaException(e,sys) from e

    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            zip_file_path =  self.download_fifa_data()
            self.extract_zip_file(zip_file_path=zip_file_path)
            return self.split_data_as_train_test()
        except Exception as e:
            raise FifaException(e,sys) from e
    


    def __del__(self):
        logging.info(f"{'>>'*20}Data Ingestion log completed.{'<<'*20} \n\n")
