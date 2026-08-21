# SyndProxy private pool

## Current pool

- Alive now: 767
- Gold now: 418
- HTTP: 199 alive / 88 gold
- HTTPS: 136 alive / 24 gold
- SOCKS4: 217 alive / 146 gold
- SOCKS5: 215 alive / 160 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27726
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
