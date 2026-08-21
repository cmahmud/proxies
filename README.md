# SyndProxy private pool

## Current pool

- Alive now: 920
- Gold now: 422
- HTTP: 274 alive / 95 gold
- HTTPS: 203 alive / 24 gold
- SOCKS4: 213 alive / 141 gold
- SOCKS5: 230 alive / 162 gold

## Historical pool

- Discovered: 159203
- Ever alive: 30167
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
