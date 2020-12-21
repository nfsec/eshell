## Version changelog ##

**Changelog (v0.7.6.2):**

- New global commands: history_file, history_search
- New "show" commands: script, script_context, script_language
- New "exec" commands: indices_split, indices_shrink, indices_clone, indices_freeze, indices_unfreeze,
  indices_delete_all, shards_allocate_replica_cancel, shards_allocate_primary_cancel
- Implemented argparse
- Update to current python-requests (v2.24.0)
- Logfile moved to ~/.e7/es.log
- Command history is saved to ~/.e7/history

**Changelog (v0.6.8.3):**

- New "show" commands: cluster_remote, cluster_state_metadata, indices_by(!), cluster_state_routing_table,
  nodes_stats_adaptive_selection, nodes_tasks_by_action, nodes_tasks_by_node
- New "exec" commands: shards_allocate_replica
- Extended commands: cluster_stats, nodes_plugins, nodes_fielddata, nodes_hot_threads
- Renamed commands:
  - cluster_allocation -> cluster_allocation_explain
  - cluster_version -> cluster_state_version
  - cluster_nodes -> cluster_state_nodes
  - cluster_blocks -> cluster_state_blocks
  - nodes_cat_fielddata_evictions -> nodes_cat_fielddata_and_evictions
  - nodes_cat_query_cache_evictions -> nodes_cat_query_cache_and_evictions
  - nodes_cat_request_cache_evictions -> nodes_cat_request_cache_and_evictions
  - nodes_cat_index -> nodes_cat_indexing
- Update to current python-requests (v2.22.0)
- Logfile moved to ~/.eshell/es.log
- Command history is saved to ~/.eshell/history

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
