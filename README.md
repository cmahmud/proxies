# SyndProxy private pool

## Current pool

- Alive now: 969
- Gold now: 444
- HTTP: 311 alive / 99 gold
- HTTPS: 192 alive / 35 gold
- SOCKS4: 199 alive / 148 gold
- SOCKS5: 267 alive / 162 gold

## Historical pool

- Discovered: 153739
- Ever alive: 28686
- Ever gold: 1112

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
