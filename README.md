# SyndProxy private pool

## Current pool

- Alive now: 1081
- Gold now: 407
- HTTP: 334 alive / 78 gold
- HTTPS: 257 alive / 22 gold
- SOCKS4: 224 alive / 151 gold
- SOCKS5: 266 alive / 156 gold

## Historical pool

- Discovered: 165751
- Ever alive: 32292
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
