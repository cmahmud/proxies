# SyndProxy private pool

## Current pool

- Alive now: 994
- Gold now: 366
- HTTP: 328 alive / 79 gold
- HTTPS: 215 alive / 25 gold
- SOCKS4: 215 alive / 124 gold
- SOCKS5: 236 alive / 138 gold

## Historical pool

- Discovered: 165816
- Ever alive: 32320
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
