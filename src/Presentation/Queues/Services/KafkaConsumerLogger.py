import logging

class KafkaConsumerLogger:
    @staticmethod
    def set_logger() -> logging.Logger:
        arify_consumer_logger = logging.getLogger('ExampleFakeApiInfra.ExampleFakeApiInfra')
        arify_consumer_logger.setLevel(logging.INFO)

        # Create console handler if it doesn't exist
        if not arify_consumer_logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(formatter)
            arify_consumer_logger.addHandler(console_handler)
        
        return arify_consumer_logger

# # Configure logger specific to Queues module
# arify_consumer_logger = logging.getLogger('Presentation.Queues')
# arify_consumer_logger.setLevel(logging.INFO)

# # Create console handler if it doesn't exist
# if not arify_consumer_logger.handlers:
#     console_handler = logging.StreamHandler()
#     console_handler.setLevel(logging.INFO)
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     console_handler.setFormatter(formatter)
#     arify_consumer_logger.addHandler(console_handler)