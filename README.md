# Strategy Evaluation Pipeline

### Daily automated workflow:
- Fetch the latest market data
- Run multiple strategies in batch (with different parameters)
- Compute performance metrics (Sharpe ratio / drawdown / win rate etc.)
- Store results in S3 (data lake)
- Make data available for analysis and visualization

### Architecture overview
````
Airflow (Scheduler) 
↓ 
Trigger ECS Tasks (parallel) 
↓ 
Docker Container (Backtesting Engine) 
↓ 
Load data from S3 
↓ 
Run strategies (backtesting.py) 
↓ 
Write results → S3 
↓ 
Athena / Pandas analysis
````
### Code structure:

- **main.py** – Entry point for ECS tasks; orchestrates loading data, running strategies, and writing results.
- **config/strategies.yml** – Declarative configuration for strategies and their parameters, enabling flexible experimentation without changing code.
- **engine/loader.py** – Handles reading raw or processed market data from S3.
- **engine/writer.py** – Handles writing strategy outputs, and metrics to the appropriate S3 location in a structured format.
- **indicators/** – Collection of reusable technical indicators; decoupled from strategies for modularity and testability.
- **strategies/** – Implements trading logic (buy/sell decisions); can consume indicators from indicators/ to build composite signals.