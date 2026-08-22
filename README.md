# SyndProxy private pool

## Current pool

- Alive now: 1151
- Gold now: 372
- HTTP: 438 alive / 82 gold
- HTTPS: 270 alive / 23 gold
- SOCKS4: 175 alive / 105 gold
- SOCKS5: 268 alive / 162 gold

## Historical pool

- Discovered: 166635
- Ever alive: 32471
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
