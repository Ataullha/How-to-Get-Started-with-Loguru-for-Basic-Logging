### Getting Started with Loguru for Basic Logging in Python

As a beginner in Python, especially in fields like machine learning, it's common to rely on `print` statements for tracking code flow and debugging. However, as projects grow in complexity, using `print` becomes problematic—cluttering your code and making error tracing in a production environment challenging.

**The Solution? Logging.**

Logging provides a cleaner, more structured way to monitor your application, helping you catch errors, track events, and understand what your code is doing in real-time without polluting your codebase with `print` statements. And that's where **Loguru** comes in, offering a simple, powerful way to handle logging in Python.

---

### Why Use Loguru Over Print Statements?

Loguru makes logging easy and is especially handy for those new to Python. Its key benefits include:

- **Cleaner Code**: Loguru eliminates the need for scattered `print` statements, giving you clean and organized logs.
- **Multiple Levels of Logging**: You can log messages with varying importance—INFO, DEBUG, ERROR, etc.
- **Automatic Exception Logging**: The `@logger.catch` decorator catches exceptions and logs full context, making error handling a breeze.

---

### Quick Start with Loguru

Let’s dive into how to set up Loguru for basic logging. Below is a minimal example of configuring Loguru to log messages to a file with custom formatting.

```python
from loguru import logger

# Remove the default logger to customize
logger.remove()

# Set up a new logging configuration
logger.add("logs/{time:YYYY-MM-DD}.log",  # Log file path, creates a new log each day
           format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | "
                  "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
           level="INFO")  # Only logs INFO level and above
```

Here’s a breakdown of the configuration:

- **File Path**: `"logs/{time:YYYY-MM-DD}.log"` dynamically creates a new log file daily, naming it by date.
- **Formatting**:
  - `<green>{time:YYYY-MM-DD HH:mm:ss}</green>`: Timestamp in green.
  - `<level>{level: <8}</level>`: Log level, like INFO or ERROR, left-aligned and styled.
  - `<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>`: Shows the module name, function, and line number.
  - `<level>{message}</level>`: The actual log message, styled based on its level.
- **Log Level**: `level="INFO"` limits log output to INFO and above (WARNING, ERROR, etc.), excluding DEBUG for conciseness.

---

### Logging Basic Events with Loguru

Loguru supports various log levels. Here’s how you can log messages at different levels:

```python
# Basic log levels in Loguru
logger.info("This is an info log")          # General info
logger.debug("This is a debug log")          # Debugging info (won't appear due to "INFO" level)
logger.warning("This is a warning log")      # Warnings
logger.error("This is an error log")         # Errors
logger.critical("This is a critical log")    # Serious errors
logger.success("This is a success log")      # Successful completion messages
logger.exception("This is an exception log") # Logs the stack trace for exceptions
```

Each level helps you categorize logs, making it easier to monitor code execution and catch potential issues.

---

### Automatically Catching Exceptions with `@logger.catch`

Loguru’s `@logger.catch` decorator is a standout feature. It wraps your functions to catch any unhandled exceptions and log the error details automatically. Here’s how it works:

```python
@logger.catch
def divide(x, y):
    return x / y

# Attempting to divide by zero
divide(1, 0)
```

In this example, attempting to divide by zero will raise an exception. The `@logger.catch` decorator logs the exception with the stack trace, making it easier to debug without adding extra error-handling code.

---

### Putting It All Together: A Sample Script

Here’s a complete example using Loguru to log different events, handle exceptions, and configure daily log files.

```python
from loguru import logger

# Remove default logger to set custom configuration
logger.remove()

# Set up a new logging configuration
logger.add("logs/{time:YYYY-MM-DD}.log",
           format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | "
                  "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
           level="INFO")

@logger.catch
def divide(x, y):
    return x / y

def main():
    # Log various messages at different levels
    logger.info("This is an info log")
    logger.debug("This is a debug log")
    logger.error("This is an error log")
    logger.warning("This is a warning log")
    logger.critical("This is a critical log")
    logger.success("This is a success log")
    
    # Test exception logging
    divide(1, 0)

if __name__ == "__main__":
    main()
```

This script configures Loguru to:
1. Log messages to a daily file with custom formatting.
2. Log messages at multiple levels to illustrate their use.
3. Catch and log exceptions in the `divide` function.

---

### Advanced Tips for Customizing Loguru

Here are a few additional tricks to make the most of Loguru:

1. **Daily Log Files**: Use `{time:YYYY-MM-DD}.log` to generate a new log file each day automatically.
2. **Console Logging**: If you want logs to display in the console, comment out `logger.remove()`. This keeps the default console logger active.
3. **Contextual Logging with `bind`**: You can use `logger.bind` to add custom attributes for specific sessions or operations. This is helpful when you need additional context, such as a user ID, in each log entry.
   
   ```python
   from loguru import logger
   import time
   
   # Configure logger
   logger.add("logs/{time:YYYY-MM-DD}.log",
              format="<green>{time}</green> | ID: <yellow>{extra[chat_id]}</yellow> | <level>{message}</level>",
              level="INFO")
   
   # Bind custom attributes
   chat_logger = logger.bind(chat_id=time.time())
   chat_logger.info("Bound log with custom chat_id")
   ```

---

### Why Use Loguru for Python Logging?

Compared to Python’s built-in `logging` module, Loguru is:
- **Easier to Set Up**: It’s ready-to-use out of the box.
- **More Readable**: Log formatting and coloring improve readability.
- **Flexible for Exception Handling**: The `@logger.catch` decorator simplifies exception logging.

Loguru’s simplicity combined with powerful features makes it ideal for Python beginners and pros alike. Whether you’re working on a small script or a full-scale application, using Loguru instead of `print` will enhance your ability to monitor and debug effectively.

---

### Final Thoughts

Switching from `print` statements to Loguru’s structured logging is a game-changer, particularly for larger projects or those moving to production. By setting up custom formats, automatic exception handling, and daily logs, Loguru provides an organized and powerful way to track your application's behavior. For data science, machine learning, or general Python projects, Loguru is an efficient tool that will keep your logging clean and concise.

Happy Logging!
