# SyndProxy private pool

## Current pool

- Alive now: 1002
- Gold now: 374
- HTTP: 341 alive / 79 gold
- HTTPS: 237 alive / 25 gold
- SOCKS4: 172 alive / 106 gold
- SOCKS5: 252 alive / 164 gold

## Historical pool

- Discovered: 166635
- Ever alive: 32471
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
