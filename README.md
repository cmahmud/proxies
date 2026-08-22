# SyndProxy private pool

## Current pool

- Alive now: 927
- Gold now: 367
- HTTP: 287 alive / 79 gold
- HTTPS: 207 alive / 22 gold
- SOCKS4: 202 alive / 138 gold
- SOCKS5: 231 alive / 128 gold

## Historical pool

- Discovered: 165836
- Ever alive: 32363
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
