# SyndProxy private pool

## Current pool

- Alive now: 904
- Gold now: 409
- HTTP: 296 alive / 88 gold
- HTTPS: 168 alive / 25 gold
- SOCKS4: 223 alive / 148 gold
- SOCKS5: 217 alive / 148 gold

## Historical pool

- Discovered: 166322
- Ever alive: 32387
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
