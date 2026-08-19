# SyndProxy private pool

## Current pool

- Alive now: 972
- Gold now: 362
- HTTP: 309 alive / 64 gold
- HTTPS: 215 alive / 19 gold
- SOCKS4: 219 alive / 125 gold
- SOCKS5: 229 alive / 154 gold

## Historical pool

- Discovered: 109991
- Ever alive: 15658
- Ever gold: 499

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
