# SyndProxy private pool

## Current pool

- Alive now: 992
- Gold now: 222
- HTTP: 404 alive / 34 gold
- HTTPS: 156 alive / 10 gold
- SOCKS4: 245 alive / 103 gold
- SOCKS5: 187 alive / 75 gold

## Historical pool

- Discovered: 86675
- Ever alive: 6452
- Ever gold: 296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
