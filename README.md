# SyndProxy private pool

## Current pool

- Alive now: 985
- Gold now: 361
- HTTP: 324 alive / 64 gold
- HTTPS: 176 alive / 15 gold
- SOCKS4: 250 alive / 156 gold
- SOCKS5: 235 alive / 126 gold

## Historical pool

- Discovered: 110866
- Ever alive: 16024
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
