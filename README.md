# SyndProxy private pool

## Current pool

- Alive now: 1070
- Gold now: 341
- HTTP: 387 alive / 62 gold
- HTTPS: 216 alive / 11 gold
- SOCKS4: 246 alive / 141 gold
- SOCKS5: 221 alive / 127 gold

## Historical pool

- Discovered: 129268
- Ever alive: 20248
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
