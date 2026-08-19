# SyndProxy private pool

## Current pool

- Alive now: 1062
- Gold now: 522
- HTTP: 369 alive / 161 gold
- HTTPS: 258 alive / 89 gold
- SOCKS4: 215 alive / 140 gold
- SOCKS5: 220 alive / 132 gold

## Historical pool

- Discovered: 119875
- Ever alive: 18521
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
