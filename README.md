# SyndProxy private pool

## Current pool

- Alive now: 868
- Gold now: 272
- HTTP: 287 alive / 34 gold
- HTTPS: 163 alive / 8 gold
- SOCKS4: 248 alive / 138 gold
- SOCKS5: 170 alive / 92 gold

## Historical pool

- Discovered: 102899
- Ever alive: 13904
- Ever gold: 431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
