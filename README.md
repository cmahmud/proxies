# SyndProxy private pool

## Current pool

- Alive now: 930
- Gold now: 422
- HTTP: 281 alive / 94 gold
- HTTPS: 199 alive / 25 gold
- SOCKS4: 220 alive / 141 gold
- SOCKS5: 230 alive / 162 gold

## Historical pool

- Discovered: 159203
- Ever alive: 30168
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
