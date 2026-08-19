# SyndProxy private pool

## Current pool

- Alive now: 1239
- Gold now: 387
- HTTP: 405 alive / 87 gold
- HTTPS: 269 alive / 15 gold
- SOCKS4: 252 alive / 144 gold
- SOCKS5: 313 alive / 141 gold

## Historical pool

- Discovered: 133967
- Ever alive: 21693
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
