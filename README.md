# SyndProxy private pool

## Current pool

- Alive now: 892
- Gold now: 456
- HTTP: 269 alive / 124 gold
- HTTPS: 191 alive / 45 gold
- SOCKS4: 214 alive / 146 gold
- SOCKS5: 218 alive / 141 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16783
- Ever gold: 624

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
