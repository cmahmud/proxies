# SyndProxy private pool

## Current pool

- Alive now: 847
- Gold now: 363
- HTTP: 227 alive / 74 gold
- HTTPS: 185 alive / 23 gold
- SOCKS4: 196 alive / 131 gold
- SOCKS5: 239 alive / 135 gold

## Historical pool

- Discovered: 157406
- Ever alive: 29657
- Ever gold: 1134

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
