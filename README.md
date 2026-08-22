# SyndProxy private pool

## Current pool

- Alive now: 1035
- Gold now: 391
- HTTP: 360 alive / 82 gold
- HTTPS: 216 alive / 25 gold
- SOCKS4: 215 alive / 128 gold
- SOCKS5: 244 alive / 156 gold

## Historical pool

- Discovered: 166564
- Ever alive: 32410
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
