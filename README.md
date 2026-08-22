# SyndProxy private pool

## Current pool

- Alive now: 992
- Gold now: 374
- HTTP: 311 alive / 80 gold
- HTTPS: 276 alive / 27 gold
- SOCKS4: 185 alive / 125 gold
- SOCKS5: 220 alive / 142 gold

## Historical pool

- Discovered: 165756
- Ever alive: 32309
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
