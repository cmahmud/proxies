# SyndProxy private pool

## Current pool

- Alive now: 638
- Gold now: 345
- HTTP: 157 alive / 63 gold
- HTTPS: 112 alive / 18 gold
- SOCKS4: 180 alive / 130 gold
- SOCKS5: 189 alive / 134 gold

## Historical pool

- Discovered: 147017
- Ever alive: 25756
- Ever gold: 1075

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
