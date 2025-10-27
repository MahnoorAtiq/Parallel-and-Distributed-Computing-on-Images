# Parallel-and-Distributed-Computing-on-Images

This project demonstrates parallel and distributed image processing using Python’s multiprocessing module. It simulates a distributed environment with two “nodes” on a single machine using multiprocessing.Manager() and Queue. Each node processes its subset of images, and the master process aggregates and reports total processing times.

Features:
Sequential Processing: Baseline single-process execution.
Parallel Processing: Utilizes multiple worker processes (1, 2, 4, 8) for concurrent image handling.
Distributed Simulation: Simulates two logical nodes processing separate subsets of images.
Performance Measurement: Records and compares execution times for each configuration.
Scalable Design: Can be extended to real distributed systems with minimal changes.

Configuration
Method	     Configuration	    Execution Time
Sequential	 Single Process    	0.56 seconds
Parallel      	1 worker	      0.25 seconds
Parallel      	2 workers	      0.11 seconds
Parallel	      4 workers	      0.08 seconds
Parallel	      8 workers	      0.07 seconds
Distributed	    2 Nodes       	1.64 seconds

Performance Summary:
Best performance was achieved with 4 workers (0.07 seconds), providing optimal CPU utilization.
Increasing workers beyond 4 caused minor slowdowns due to context-switching overhead.
The distributed mode introduced extra coordination time, resulting in slightly higher execution time than parallel mode.
Parallel processing on a single machine is faster for small workloads, while distributed systems are more beneficial for larger datasets.
