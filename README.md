# SyndProxy private pool

## Current pool

- Alive now: 1138
- Gold now: 368
- HTTP: 411 alive / 79 gold
- HTTPS: 292 alive / 23 gold
- SOCKS4: 178 alive / 105 gold
- SOCKS5: 257 alive / 161 gold

## Historical pool

- Discovered: 166635
- Ever alive: 32471
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
