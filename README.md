# SyndProxy private pool

## Current pool

- Alive now: 1024
- Gold now: 396
- HTTP: 317 alive / 71 gold
- HTTPS: 224 alive / 16 gold
- SOCKS4: 245 alive / 148 gold
- SOCKS5: 238 alive / 161 gold

## Historical pool

- Discovered: 129319
- Ever alive: 20471
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
