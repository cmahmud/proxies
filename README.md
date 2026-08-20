# SyndProxy private pool

## Current pool

- Alive now: 1449
- Gold now: 615
- HTTP: 558 alive / 220 gold
- HTTPS: 433 alive / 115 gold
- SOCKS4: 219 alive / 135 gold
- SOCKS5: 239 alive / 145 gold

## Historical pool

- Discovered: 141134
- Ever alive: 23801
- Ever gold: 961

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
