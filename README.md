# SyndProxy private pool

## Current pool

- Alive now: 1035
- Gold now: 475
- HTTP: 337 alive / 121 gold
- HTTPS: 235 alive / 72 gold
- SOCKS4: 217 alive / 140 gold
- SOCKS5: 246 alive / 142 gold

## Historical pool

- Discovered: 114270
- Ever alive: 16914
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
