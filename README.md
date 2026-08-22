# SyndProxy private pool

## Current pool

- Alive now: 1037
- Gold now: 389
- HTTP: 359 alive / 80 gold
- HTTPS: 214 alive / 25 gold
- SOCKS4: 215 alive / 128 gold
- SOCKS5: 249 alive / 156 gold

## Historical pool

- Discovered: 166564
- Ever alive: 32407
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
