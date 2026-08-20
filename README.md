# SyndProxy private pool

## Current pool

- Alive now: 1051
- Gold now: 400
- HTTP: 360 alive / 90 gold
- HTTPS: 273 alive / 23 gold
- SOCKS4: 195 alive / 134 gold
- SOCKS5: 223 alive / 153 gold

## Historical pool

- Discovered: 144729
- Ever alive: 24925
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
