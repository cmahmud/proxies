# SyndProxy private pool

## Current pool

- Alive now: 788
- Gold now: 231
- HTTP: 220 alive / 30 gold
- HTTPS: 118 alive / 8 gold
- SOCKS4: 235 alive / 110 gold
- SOCKS5: 215 alive / 83 gold

## Historical pool

- Discovered: 86774
- Ever alive: 7592
- Ever gold: 338

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
