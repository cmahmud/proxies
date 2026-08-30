# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 438
- HTTP: 114 alive / 84 gold
- HTTPS: 54 alive / 24 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 200 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44550
- Ever gold: 1405

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
