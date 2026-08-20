# SyndProxy private pool

## Current pool

- Alive now: 1572
- Gold now: 583
- HTTP: 574 alive / 196 gold
- HTTPS: 444 alive / 99 gold
- SOCKS4: 254 alive / 138 gold
- SOCKS5: 300 alive / 150 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23329
- Ever gold: 917

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
