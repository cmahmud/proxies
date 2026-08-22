# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 390
- HTTP: 360 alive / 79 gold
- HTTPS: 214 alive / 26 gold
- SOCKS4: 211 alive / 128 gold
- SOCKS5: 246 alive / 157 gold

## Historical pool

- Discovered: 166564
- Ever alive: 32407
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
