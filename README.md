# SyndProxy private pool

## Current pool

- Alive now: 1492
- Gold now: 426
- HTTP: 580 alive / 115 gold
- HTTPS: 351 alive / 21 gold
- SOCKS4: 244 alive / 137 gold
- SOCKS5: 317 alive / 153 gold

## Historical pool

- Discovered: 136248
- Ever alive: 22676
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
