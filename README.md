## Elasticsearch Interactive Shell ##

EShell is a Python script that allows you to interact from command-line with a running [elasticsearch](https://www.elastic.co/products/elasticsearch)
cluster using the APIs over HTTP. HTTP Basic Authentication is supported by the environment variable **$ESAUTH** in the format: **login:password**.

> v0.3.12 tested under Elasticsearch v1.7.5

**Example:**

```
(eshell)stardust~$ ./eshell localhost.localdomain
Connecting to elasticsearch server at address: localhost.localdomain
Connected to: localhost.localdomain on port: 9200

### Welcome to elasticsearch console!
### For more information, type 'help'

es:~$ show

Entering to cluster information menu.

es:show~$ cluster_health
status: green
number_of_nodes: 33
unassigned_shards: 0
number_of_pending_tasks: 0
number_of_in_flight_fetch: 0
timed_out: False
active_primary_shards: 11864
cluster_name: darkstar
relocating_shards: 0
active_shards: 18382
initializing_shards: 0
number_of_data_nodes: 20
delayed_unassigned_shards: 0

es:show~$ indices_size
i <= 1.MB: 2092 | i <= 10.MB: 1490 | i <= 100.MB: 1195 | i <= 1.GB: 1036 | i <= 10.GB: 811 | i <= 100.GB: 584 | i >= 100.GB: 89

es:show~$ shards_allocation esdatanode1.lan
shards disk.used disk.avail disk.total disk.percent host             ip          node
   744     3.7tb      4.2tb        8tb           46 esdatanode1.lan  10.1.2.1    esdatanode1.lan
```

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

