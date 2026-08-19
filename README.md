# SyndProxy private pool

## Current pool

- Alive now: 1089
- Gold now: 525
- HTTP: 396 alive / 159 gold
- HTTPS: 251 alive / 90 gold
- SOCKS4: 220 alive / 140 gold
- SOCKS5: 222 alive / 136 gold

## Historical pool

- Discovered: 119875
- Ever alive: 18523
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
