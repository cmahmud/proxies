# SyndProxy private pool

## Current pool

- Alive now: 1218
- Gold now: 439
- HTTP: 419 alive / 110 gold
- HTTPS: 320 alive / 29 gold
- SOCKS4: 224 alive / 151 gold
- SOCKS5: 255 alive / 149 gold

## Historical pool

- Discovered: 153722
- Ever alive: 28558
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
