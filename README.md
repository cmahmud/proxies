# SyndProxy private pool

## Current pool

- Alive now: 866
- Gold now: 276
- HTTP: 296 alive / 37 gold
- HTTPS: 161 alive / 8 gold
- SOCKS4: 241 alive / 137 gold
- SOCKS5: 168 alive / 94 gold

## Historical pool

- Discovered: 102899
- Ever alive: 13908
- Ever gold: 432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
