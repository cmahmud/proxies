# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 360
- HTTP: 77 alive / 54 gold
- HTTPS: 53 alive / 13 gold
- SOCKS4: 166 alive / 151 gold
- SOCKS5: 173 alive / 142 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43483
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
