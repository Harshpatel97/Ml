from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.pipeline.stage_04_model_trainer import ModeltrainingPipeline
from src.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
from src.logging import logger


STAGE_NAME = 'Data Ingestion'

try:
    logger.info(f">>>>>>>{STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME1 = 'Data Validation'

try:
    logger.info(f">>>>>>>{STAGE_NAME} started <<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME1} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME2 = 'Data Transformation'

try:
    logger.info(f">>>>>>>{STAGE_NAME2} started <<<<<<<")
    data_transformation= DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME2} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME3 = 'Model Trainer'

try:
    logger.info(f">>>>>>>{STAGE_NAME3} started <<<<<<<")
    model_trainer= ModeltrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME3} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME4 = 'Model Evaluation'

try:
    logger.info(f">>>>>>>{STAGE_NAME4} started <<<<<<<")
    model_evaluation= ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>> stage {STAGE_NAME4} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e