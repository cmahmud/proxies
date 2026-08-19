# SyndProxy private pool

## Current pool

- Alive now: 898
- Gold now: 492
- HTTP: 270 alive / 122 gold
- HTTPS: 188 alive / 70 gold
- SOCKS4: 215 alive / 151 gold
- SOCKS5: 225 alive / 149 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16783
- Ever gold: 624

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
