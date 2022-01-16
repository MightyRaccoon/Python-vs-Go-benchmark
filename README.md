Python vs Go benchmark

Benchmark that con show which language is yhe most suitable for business simulation system.

## Test №1: Server for data reading from DB.

Let's say we have a table in PostgreSQL and we want a service that allows us to read data by ID from. There are several choices for realizations:
1. Sync Python service
2. Async Python 
3. Sync Go
4. Async Go

The quality metrics are:
1. Average response time
2. 90-th response time percentile
3. 95-th response time percentile
4. 99-th response time percentile
5. Response time distributions
