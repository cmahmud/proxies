# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 381
- HTTP: 89 alive / 66 gold
- HTTPS: 100 alive / 13 gold
- SOCKS4: 155 alive / 145 gold
- SOCKS5: 178 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43237
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
