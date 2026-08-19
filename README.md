# SyndProxy private pool

## Current pool

- Alive now: 1030
- Gold now: 344
- HTTP: 373 alive / 64 gold
- HTTPS: 202 alive / 12 gold
- SOCKS4: 237 alive / 141 gold
- SOCKS5: 218 alive / 127 gold

## Historical pool

- Discovered: 129268
- Ever alive: 20246
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
