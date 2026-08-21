# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 407
- HTTP: 338 alive / 101 gold
- HTTPS: 193 alive / 21 gold
- SOCKS4: 215 alive / 133 gold
- SOCKS5: 265 alive / 152 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27934
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
