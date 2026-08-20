# SyndProxy private pool

## Current pool

- Alive now: 900
- Gold now: 432
- HTTP: 222 alive / 87 gold
- HTTPS: 187 alive / 20 gold
- SOCKS4: 225 alive / 158 gold
- SOCKS5: 266 alive / 167 gold

## Historical pool

- Discovered: 151674
- Ever alive: 27587
- Ever gold: 1100

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
