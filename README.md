# SyndProxy private pool

## Current pool

- Alive now: 922
- Gold now: 397
- HTTP: 280 alive / 86 gold
- HTTPS: 186 alive / 26 gold
- SOCKS4: 216 alive / 137 gold
- SOCKS5: 240 alive / 148 gold

## Historical pool

- Discovered: 163863
- Ever alive: 31977
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
