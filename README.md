# SyndProxy private pool

## Current pool

- Alive now: 1153
- Gold now: 407
- HTTP: 379 alive / 81 gold
- HTTPS: 233 alive / 14 gold
- SOCKS4: 274 alive / 153 gold
- SOCKS5: 267 alive / 159 gold

## Historical pool

- Discovered: 131718
- Ever alive: 20691
- Ever gold: 873

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
