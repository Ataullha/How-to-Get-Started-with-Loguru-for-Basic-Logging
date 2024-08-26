from loguru import logger

# remove default logger
logger.remove()

# logger configuration
logger.add("log_folder/{time:YYYY-MM-DD}.log",
           format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
           level="INFO")

# exception log from @logger.catch decorator
@logger.catch
def divide(x, y):
    return x / y

# differnt log level
def main():
    
    # other basic logging level
    logger.info("This is a info log")
    logger.debug("This is a debug log")
    logger.error("This is a error log") 
    logger.warning("This is a warning log")
    logger.critical("This is a critical log")
    logger.success("This is a success log")
    logger.exception("This is a exception log")
    
    # exception log for function divide
    divide(1,0)

# main function
if __name__ == "__main__":
    main()