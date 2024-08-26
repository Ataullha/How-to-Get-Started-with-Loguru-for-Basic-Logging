### How to Get Started with Loguru for Basic Logging

As a beginner in Python, especially in the field of machine learning, it’s common to rely heavily on `print` statements for debugging and tracking the flow of your code. However, as projects grow in complexity, this approach can become problematic. Print statements can clutter your code and make it difficult to trace issues in a production environment. 

**The Solution? Logging.**

Logging is a powerful way to monitor your application. It allows you to keep track of events, catch exceptions, and understand what your code is doing in real-time—all without polluting your codebase with `print` statements.



```python
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

if __name__ == "__main__":
    main()
```

### Explanation

```python
from loguru import logger
```
- **Explanation**: Imports the `logger` object from the `loguru` library. `loguru` is a powerful and easy-to-use logging library in Python.

---

```python
# remove default logger
logger.remove()
```
- **Explanation**: Removes the default logger that `loguru` sets up. This is done to customize the logger configuration according to specific requirements.

---

```python
# logger configuration
logger.add("log_folder/{time:YYYY-MM-DD}.log",
           format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
           level="INFO")
```
- **Explanation**: Adds a new logging configuration to the `logger`:
  - **`"log_folder/{time:YYYY-MM-DD}.log"`**: Specifies the log file's path and name. The `{time:YYYY-MM-DD}` part dynamically generates the log file name based on the current date, creating a new log file each day.
  - **`format`**: Defines the format of the log messages. It uses the following format specifiers:
    - **`<green>{time:YYYY-MM-DD HH:mm:ss}</green>`**: The timestamp of the log entry, formatted as `YYYY-MM-DD HH:mm:ss` and colored green.
    - **`<level>{level: <8}</level>`**: The log level (e.g., INFO, ERROR), left-aligned within 8 characters and styled according to its level.
    - **`<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>`**: The logger name, function name, and line number from where the log entry was made, all colored cyan.
    - **`- <level>{message}</level>`**: The log message itself, styled according to its level.
  - **`level="INFO"`**: Sets the minimum log level to `INFO`, meaning only log entries of level `INFO` or higher (WARNING, ERROR, etc.) will be recorded.

---

```python
# exception log from @logger.catch decorator
@logger.catch
def divide(x, y):
    return x / y
```
- **Explanation**: Defines a function `divide` that takes two arguments, `x` and `y`, and returns the result of dividing `x` by `y`.
  - **`@logger.catch`**: This decorator catches any exceptions raised in the function and logs the exception details. If an exception occurs (e.g., dividing by zero), it will be logged with all relevant information, including the stack trace.

---

```python
    # other basic logging levels
    logger.info("This is an info log")
    logger.debug("This is a debug log")
    logger.error("This is an error log") 
    logger.warning("This is a warning log")
    logger.critical("This is a critical log")
    logger.success("This is a success log")
    logger.exception("This is an exception log")
```
- **Explanation**: Logs messages at various levels to demonstrate their usage:
  - **`logger.info("This is an info log")`**: Logs an informational message, useful for general output or tracking the flow of the application.
  - **`logger.debug("This is a debug log")`**: Logs a debug message, typically used for development and troubleshooting purposes (note: it won't appear in the log file since the configured level is `INFO`).
  - **`logger.error("This is an error log")`**: Logs an error message, indicating that something went wrong in the application.
  - **`logger.warning("This is a warning log")`**: Logs a warning message, signaling a potential issue that may require attention.
  - **`logger.critical("This is a critical log")`**: Logs a critical message, which indicates a severe error that might cause the program to terminate.
  - **`logger.success("This is a success log")`**: Logs a success message, used to indicate that an operation has been successfully completed.
  - **`logger.exception("This is an exception log")`**: Logs an exception message. This is similar to `logger.error` but also logs the stack trace of the most recent exception, which is useful for debugging.

---

```python
    # exception log for function divide
    divide(1, 0)
```
- **Explanation**: Calls the `divide` function with arguments `1` and `0`. This will raise a `ZeroDivisionError`, which is caught by the `@logger.catch` decorator, and the exception details are logged.

---

```python
# main function
if __name__ == "__main__":
    main()
```
- **Explanation**: This is a standard Python construct that ensures the `main()` function is called only when the script is run directly, not when it is imported as a module. It triggers the execution of the `main` function, which in turn logs the messages and handles the division exception.
