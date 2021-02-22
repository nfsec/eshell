## Elasticsearch Interactive Shell ##

EShell is a Python script that allows you to interact from command-line with a running [elasticsearch](https://www.elastic.co/products/elasticsearch)
cluster using the APIs over HTTP. The official low-level [client](https://github.com/elastic/elasticsearch-py) is used for communication.

> v0.7.10.2 tested under Elasticsearch v7.10.2

**Example:**

```
(eshell) stardust~$ eshell -h
usage: eshell [-h] [-a] [-p PORT] [host]

example: eshell elasticsearch.lan

positional arguments:
  host                  elasticsearch IP or hostname (default: 127.0.0.1)

optional arguments:
  -h, --help            show this help message and exit
  -a, --auth            use login and password
  -p PORT, --port PORT  elasticsearch http port (default: 9200)

:: ES7shell

(eshell) stardust~$ eshell localhost.localdomain
Connecting to elasticsearch server at address: localhost.localdomain
Connected to: localhost.localdomain on port: 9200

### Welcome to elasticsearch shell console!
### For more information, type "help" or "?".
### Session will be logged to ~/.e7/es.log.
### Command history will be saved to ~/.e7/history.

e7:~$ show

### Entering to cluster information menu!
### For more information, type "help" or "?".

es7:show~$ help cluster_health

        Get a very simple status on the health of the cluster.
        $ cluster_health - show cluster health.
        $ cluster_health [table] - one-line representation of the same information from cluster_health.

es7:show~$ cluster_health

   active_primary_shards: 19
   active_shards: 40
   active_shards_percent_as_number: 100.0
   cluster_name: darkstar
   delayed_unassigned_shards: 0
   initializing_shards: 0
   number_of_data_nodes: 4
   number_of_in_flight_fetch: 0
   number_of_nodes: 4
   number_of_pending_tasks: 0
   relocating_shards: 0
   status: green
   task_max_waiting_in_queue_millis: 0
   timed_out: False
   unassigned_shards: 0

es7:show~$ cluster_remote

 dcX:
     connected: True
     http_addresses: 10.10.18.22:9201, 10.10.22.29:9202, 10.10.16.40:9333
     initial_connect_timeout: 30s
     max_connections_per_cluster: 3
     num_nodes_connected: 3
     seeds: log-master1.local:9303, log-master2.local:9303, log-master3.local:9303
     skip_unavailable: True
 dcY:
     connected: True
     http_addresses: 10.10.32.16:9202, 10.10.24.16:9201, 10.10.24.10:9333
     initial_connect_timeout: 30s
     max_connections_per_cluster: 3
     num_nodes_connected: 3
     seeds: log-master1.net:9303, log-master2.net:9303, log-master2.net:9303
     skip_unavailable: True

es7:show~$ nodes_cat_heap

name      ip           id   heap.current heap.percent heap.max
darkstar1 10.55.96.69  tL9l        1.6gb           37    4.3gb
darkstar2 10.55.96.176 L-Kb        1.7gb           40    4.3gb
darkstar3 10.55.96.179 D6p3      915.8mb           20    4.3gb
darkstar4 10.55.96.178 igw_        1.9gb           44    4.3gb

es7:show~$ indices_size
i <= 1.MB: 2092 | i <= 10.MB: 1490 | i <= 100.MB: 1195 | i <= 1.GB: 1036 | i <= 10.GB: 811 | i <= 100.GB: 584 | i >= 100.GB: 89

es7:exec~$ indices_delete .monitoring-kibana-2-2017.01.27
```
