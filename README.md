# SyndProxy private pool

## Current pool

- Alive now: 1051
- Gold now: 374
- HTTP: 375 alive / 83 gold
- HTTPS: 276 alive / 25 gold
- SOCKS4: 176 alive / 115 gold
- SOCKS5: 224 alive / 151 gold

## Historical pool

- Discovered: 158226
- Ever alive: 29889
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
