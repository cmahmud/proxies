# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 536
- HTTP: 366 alive / 155 gold
- HTTPS: 238 alive / 88 gold
- SOCKS4: 218 alive / 150 gold
- SOCKS5: 209 alive / 143 gold

## Historical pool

- Discovered: 119811
- Ever alive: 18038
- Ever gold: 713

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
