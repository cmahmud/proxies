# SyndProxy private pool

## Current pool

- Alive now: 666
- Gold now: 360
- HTTP: 145 alive / 59 gold
- HTTPS: 119 alive / 18 gold
- SOCKS4: 187 alive / 142 gold
- SOCKS5: 215 alive / 141 gold

## Historical pool

- Discovered: 147648
- Ever alive: 25868
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
