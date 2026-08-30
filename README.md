# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 436
- HTTP: 115 alive / 83 gold
- HTTPS: 51 alive / 23 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 195 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44549
- Ever gold: 1405

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
