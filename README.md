# SyndProxy private pool

## Current pool

- Alive now: 972
- Gold now: 428
- HTTP: 298 alive / 95 gold
- HTTPS: 199 alive / 29 gold
- SOCKS4: 220 alive / 146 gold
- SOCKS5: 255 alive / 158 gold

## Historical pool

- Discovered: 167127
- Ever alive: 32549
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
