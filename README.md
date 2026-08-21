# SyndProxy private pool

## Current pool

- Alive now: 1097
- Gold now: 442
- HTTP: 388 alive / 107 gold
- HTTPS: 244 alive / 27 gold
- SOCKS4: 215 alive / 144 gold
- SOCKS5: 250 alive / 164 gold

## Historical pool

- Discovered: 152765
- Ever alive: 28399
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
