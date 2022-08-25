
from fifa_rating.config.configuration import Configuartion
from fifa_rating.logger import logging
from fifa_rating.exception import FifaException
import sys

from fifa_rating.entity.artifact_entity import DataIngestionArtifact
from fifa_rating.entity.config_entity import DataIngestionConfig, ModelEvaluationConfig
from fifa_rating.component.data_ingestion import DataIngestion



class Pipeline():

    def __init__(self, config: Configuartion = Configuartion() ) -> None:
        try:
            self.config = config
        except Exception as e:
            raise FifaException(e, sys) from e

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise FifaException(e, sys) from e


    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise FifaException(e, sys) from e
