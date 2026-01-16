from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

import sys

if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(training_pipeline_config)
        dataingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        logging.info("Data ingestion Completed")
        datavalidationconfig = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(
            dataingestionartifact, datavalidationconfig)
        logging.info("Intiate Data validation")
        data_validataion_artifact = data_validation.initiate_data_validation()
        logging.info("Data validation Completed")
        logging.info("Intiate Data Transformation")
        datatransformationconfig = DataTransformationConfig(
            training_pipeline_config)
        data_transformation = DataTransformation(
            data_validation_artifact=data_validataion_artifact, data_transformation_config=datatransformationconfig)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation Completed")
        print(data_transformation_artifact)

        logging.info("Model Training sstared")
        model_trainer_config = ModelTrainerConfig(training_pipeline_config)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config,
                                     data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()

        logging.info("Model Training artifact created")

    except Exception as e:
        raise NetworkSecurityException(e, sys)
