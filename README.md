# SyndProxy private pool

## Current pool

- Alive now: 1054
- Gold now: 367
- HTTP: 361 alive / 79 gold
- HTTPS: 251 alive / 24 gold
- SOCKS4: 220 alive / 136 gold
- SOCKS5: 222 alive / 128 gold

## Historical pool

- Discovered: 165836
- Ever alive: 32360
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
