# SyndProxy private pool

## Current pool

- Alive now: 953
- Gold now: 442
- HTTP: 292 alive / 101 gold
- HTTPS: 189 alive / 30 gold
- SOCKS4: 205 alive / 149 gold
- SOCKS5: 267 alive / 162 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31068
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
