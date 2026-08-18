# SyndProxy private pool

## Current pool

- Alive now: 892
- Gold now: 276
- HTTP: 318 alive / 37 gold
- HTTPS: 189 alive / 8 gold
- SOCKS4: 220 alive / 137 gold
- SOCKS5: 165 alive / 94 gold

## Historical pool

- Discovered: 102915
- Ever alive: 13932
- Ever gold: 432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
