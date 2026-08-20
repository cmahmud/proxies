# SyndProxy private pool

## Current pool

- Alive now: 736
- Gold now: 405
- HTTP: 189 alive / 86 gold
- HTTPS: 129 alive / 22 gold
- SOCKS4: 194 alive / 129 gold
- SOCKS5: 224 alive / 168 gold

## Historical pool

- Discovered: 150985
- Ever alive: 27089
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
