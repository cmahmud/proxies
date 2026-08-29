# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 396
- HTTP: 82 alive / 66 gold
- HTTPS: 74 alive / 19 gold
- SOCKS4: 165 alive / 157 gold
- SOCKS5: 166 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43360
- Ever gold: 1370

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
