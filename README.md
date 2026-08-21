# SyndProxy private pool

## Current pool

- Alive now: 914
- Gold now: 427
- HTTP: 292 alive / 108 gold
- HTTPS: 165 alive / 33 gold
- SOCKS4: 218 alive / 138 gold
- SOCKS5: 239 alive / 148 gold

## Historical pool

- Discovered: 160258
- Ever alive: 30709
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
