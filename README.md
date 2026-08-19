# SyndProxy private pool

## Current pool

- Alive now: 904
- Gold now: 444
- HTTP: 281 alive / 124 gold
- HTTPS: 194 alive / 45 gold
- SOCKS4: 213 alive / 141 gold
- SOCKS5: 216 alive / 134 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16783
- Ever gold: 624

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
