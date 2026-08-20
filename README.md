# SyndProxy private pool

## Current pool

- Alive now: 992
- Gold now: 404
- HTTP: 341 alive / 89 gold
- HTTPS: 241 alive / 27 gold
- SOCKS4: 195 alive / 134 gold
- SOCKS5: 215 alive / 154 gold

## Historical pool

- Discovered: 144731
- Ever alive: 24931
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
