# SyndProxy private pool

## Current pool

- Alive now: 1064
- Gold now: 405
- HTTP: 326 alive / 86 gold
- HTTPS: 228 alive / 22 gold
- SOCKS4: 224 alive / 146 gold
- SOCKS5: 286 alive / 151 gold

## Historical pool

- Discovered: 156433
- Ever alive: 29535
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
