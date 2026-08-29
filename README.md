# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 396
- HTTP: 85 alive / 68 gold
- HTTPS: 74 alive / 17 gold
- SOCKS4: 159 alive / 153 gold
- SOCKS5: 171 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43311
- Ever gold: 1369

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
