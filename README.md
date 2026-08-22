# SyndProxy private pool

## Current pool

- Alive now: 1030
- Gold now: 405
- HTTP: 335 alive / 76 gold
- HTTPS: 222 alive / 20 gold
- SOCKS4: 224 alive / 150 gold
- SOCKS5: 249 alive / 159 gold

## Historical pool

- Discovered: 165751
- Ever alive: 32295
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
