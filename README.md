# SyndProxy private pool

## Current pool

- Alive now: 896
- Gold now: 257
- HTTP: 294 alive / 29 gold
- HTTPS: 166 alive / 5 gold
- SOCKS4: 211 alive / 115 gold
- SOCKS5: 225 alive / 108 gold

## Historical pool

- Discovered: 99106
- Ever alive: 11786
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
