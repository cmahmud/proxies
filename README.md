# SyndProxy private pool

## Current pool

- Alive now: 1200
- Gold now: 401
- HTTP: 385 alive / 92 gold
- HTTPS: 259 alive / 17 gold
- SOCKS4: 241 alive / 145 gold
- SOCKS5: 315 alive / 147 gold

## Historical pool

- Discovered: 133967
- Ever alive: 21757
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
