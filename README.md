# SyndProxy private pool

## Current pool

- Alive now: 1022
- Gold now: 425
- HTTP: 339 alive / 112 gold
- HTTPS: 215 alive / 34 gold
- SOCKS4: 218 alive / 136 gold
- SOCKS5: 250 alive / 143 gold

## Historical pool

- Discovered: 160275
- Ever alive: 30745
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
