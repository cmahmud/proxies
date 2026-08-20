# SyndProxy private pool

## Current pool

- Alive now: 753
- Gold now: 401
- HTTP: 181 alive / 79 gold
- HTTPS: 140 alive / 23 gold
- SOCKS4: 201 alive / 130 gold
- SOCKS5: 231 alive / 169 gold

## Historical pool

- Discovered: 150985
- Ever alive: 27084
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
