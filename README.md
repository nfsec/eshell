## Elasticsearch Interactive Shell ##

EShell is a Python script that allows you to interact from command-line with a running [elasticsearch](https://www.elastic.co/products/elasticsearch)
cluster using the APIs over HTTP. HTTP Basic Authentication is supported by the environment variable **$ESAUTH** in the format: **login:password**.

> v0.6.8.2 tested under Elasticsearch v6.8.2

**Example:**

```
(eshell)stardust~$ ./eshell localhost.localdomain
Connecting to elasticsearch server at address: localhost.localdomain
Connected to: localhost.localdomain on port: 9200

### Welcome to ElasticSearch Shell console!
### For more information, type "help" or "?".
### Session will be logged to eshell.log file.

es:~$ show

### Entering to cluster information menu!
### For more information, type "help" or "?".

es:show~$ cluster_health

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

es:show~$ nodes_cat_heap

name      ip           id   heap.current heap.percent heap.max
darkstar1 10.55.96.69  tL9l        1.6gb           37    4.3gb
darkstar2 10.55.96.176 L-Kb        1.7gb           40    4.3gb
darkstar3 10.55.96.179 D6p3      915.8mb           20    4.3gb
darkstar4 10.55.96.178 igw_        1.9gb           44    4.3gb

es:show~$ indices_size
i <= 1.MB: 2092 | i <= 10.MB: 1490 | i <= 100.MB: 1195 | i <= 1.GB: 1036 | i <= 10.GB: 811 | i <= 100.GB: 584 | i >= 100.GB: 89

es:exec~$ indices_delete .monitoring-kibana-2-2017.01.27
```
**Changelog (v0.6.8.2):**

- New "show" commands: indices_recovery, indices_segments_verbose
- ESAUTH support for login/password in input mode and CA,CRT & KEY files.

**Changelog (v0.6.3.2):**

- Update to current python-requests (v2.21.0): security (CVE-2018-18074)
- Update to current elasticsearch (v6.3.1)
- New "show" commands: indices_head, indices_tail, indices_field_caps, indices_field_termvectors, indices_search_shards, nodes_usage
- New "exec" commands: indices_create with no. of shards & replicas, indices_force_merge_only_expunge_deletes
- Others: session logging to eshell.log file & better analyzers output

**Changelog (v0.5.6.3):**

- New "show" commands: indices_field_mapping
- New "exec" commands: indices_aliases_delete, indices_aliases_create
- Update to current python-requests (v2.18.4)

**Changelog (v0.5.4.1):**

- Traceback in Exceptions
- New "show" commands: indices_field_stats, nodes_hot_threads
- New "exec" commands: cluster_reroute_retry_field_shards, indices_create, indices_create_compressed, indices_templates_delete

**Changelog (v0.5.1.2):**

- The project has been rewritten to Python 3
- Support for Elasticsearch 5.1.2

**Changelog (v0.3.12):**

- New "show" commands: cluster_version, cluster_nodes, cluster_blocks, indices_head, indices_merge
- Fixed: indices_status

**Changelog (v0.3.11):**

- Added http basic authentication by $ESAUTH environment variable. Thanks to: [geekpete](https://github.com/geekpete).

**Changelog (v0.3.10):**

- New "show" commands: cluster_ping, indices_(completion|fielddata|flush|query_cache|refresh|suggest|warmer|translog)
- New "exec" commands: templates_delete, indieces_replica_disable, indices_replica_enable, indices_cluster_cache, indices_alias
- Autocomplete in every command
- Requests update

**Changelog (v0.3.8):**

- Command "segments" is now: "indices_segments",
- New "show" commands: indices_indexing, indices_get, indices_search, nodes_filtercache, nodes_flush, nodes_get, nodes_merges, nodes_percolate, nodes_refresh, nodes_search, nodes_segments
- Upgraded "show" commands: nodes_memory, nodes_jdk, nodes_filedesc, nodes_topology
- New "exec" section with commands: indices_open, indices_close, indices_delete, indices_synced_flush, indices_optimize, nodes_shutdown

