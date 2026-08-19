# SyndProxy private pool

## Current pool

- Alive now: 956
- Gold now: 493
- HTTP: 299 alive / 119 gold
- HTTPS: 195 alive / 70 gold
- SOCKS4: 227 alive / 148 gold
- SOCKS5: 235 alive / 156 gold

## Historical pool

- Discovered: 113571
- Ever alive: 16812
- Ever gold: 624

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
