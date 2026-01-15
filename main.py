from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

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
    except Exception as e:
        raise NetworkSecurityException(e, sys)
