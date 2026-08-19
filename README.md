# SyndProxy private pool

## Current pool

- Alive now: 1010
- Gold now: 485
- HTTP: 329 alive / 122 gold
- HTTPS: 198 alive / 70 gold
- SOCKS4: 237 alive / 142 gold
- SOCKS5: 246 alive / 151 gold

## Historical pool

- Discovered: 113571
- Ever alive: 16834
- Ever gold: 624

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
