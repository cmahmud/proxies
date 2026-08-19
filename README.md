# SyndProxy private pool

## Current pool

- Alive now: 1013
- Gold now: 369
- HTTP: 326 alive / 72 gold
- HTTPS: 214 alive / 15 gold
- SOCKS4: 252 alive / 154 gold
- SOCKS5: 221 alive / 128 gold

## Historical pool

- Discovered: 110866
- Ever alive: 16031
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
