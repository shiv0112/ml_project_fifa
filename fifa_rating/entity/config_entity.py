from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig",
["dataset_download_url","zip_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])

DataValidationConfig = namedtuple("DataValidationConfig",
["schema_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig",
 ["later","transformed_train_dir","transformed_test_dir","preprocessed_object_file_path"])

ModelTrainerConfig = namedtuple("ModelTrainerConfig",
["trained_model_file_path","base_accuracy"])

ModelEvaluationConfig = namedtuple("ModelEvaluation",
["model_evaluation_file_path","time_stamp"])

ModelPusherConfig = namedtuple("MOdelPusherConfig",
["export_dir_path"])

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig",
["artifact_dir"])

