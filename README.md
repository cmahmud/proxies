# SyndProxy private pool

## Current pool

- Alive now: 954
- Gold now: 408
- HTTP: 271 alive / 97 gold
- HTTPS: 246 alive / 31 gold
- SOCKS4: 217 alive / 150 gold
- SOCKS5: 220 alive / 130 gold

## Historical pool

- Discovered: 160997
- Ever alive: 30963
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
