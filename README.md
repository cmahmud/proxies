# SyndProxy private pool

## Current pool

- Alive now: 917
- Gold now: 350
- HTTP: 295 alive / 53 gold
- HTTPS: 182 alive / 13 gold
- SOCKS4: 213 alive / 134 gold
- SOCKS5: 227 alive / 150 gold

## Historical pool

- Discovered: 107131
- Ever alive: 14910
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
