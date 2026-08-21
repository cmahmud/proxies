# SyndProxy private pool

## Current pool

- Alive now: 1036
- Gold now: 400
- HTTP: 349 alive / 79 gold
- HTTPS: 217 alive / 22 gold
- SOCKS4: 212 alive / 147 gold
- SOCKS5: 258 alive / 152 gold

## Historical pool

- Discovered: 158236
- Ever alive: 29975
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
