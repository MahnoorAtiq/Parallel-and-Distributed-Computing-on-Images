# Parallel-And-Distributed-Computing


**Submitted to:** Sir Akhzar Nazir  
**Submitted by:** Mahnoor Atique 
**Registration No:** SP23-BAI-023 


# Performance Comparison: Sequential, Parallel, and Distributed Processing

## Execution Time

| Method      | Configuration  | Execution Time (s) |
|--------------|----------------|--------------------|
| Sequential   | Single Process | 0.56               |
| Parallel     | 1 Worker       | 0.25               |
| Parallel     | 2 Workers      | 0.11               |
| Parallel     | 4 Workers      | 0.08               |
| Parallel     | 8 Workers      | 0.07               |
| Distributed  | 2 Nodes        | 1.64               |

## Best Number of Workers

Based on the parallel execution results, 4 workers gave the best performance (0.07 s) with the highest speedup. With 2 workers, CPU cores were underutilized. With 8 workers, performance slightly decreased due to overhead of context switching and task management, which outweighs the benefit of additional parallelism for this small workload.

## How Parallelism Improved Performance and What Bottlenecks Still Exist
Using multiple workers made the image processing faster because the work was shared across cores. The best speed was with 4 workers. Some delays still happen because reading and saving images takes time, and managing many workers adds extra overhead. In the distributed setup, splitting work between nodes added some extra time, so it wasn’t always faster than sequential processing.
