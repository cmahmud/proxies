# SyndProxy private pool

## Current pool

- Alive now: 1001
- Gold now: 367
- HTTP: 337 alive / 72 gold
- HTTPS: 203 alive / 15 gold
- SOCKS4: 243 alive / 154 gold
- SOCKS5: 218 alive / 126 gold

## Historical pool

- Discovered: 110866
- Ever alive: 16039
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
