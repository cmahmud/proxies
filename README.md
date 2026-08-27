# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 396
- HTTP: 86 alive / 55 gold
- HTTPS: 60 alive / 17 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 185 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41607
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
