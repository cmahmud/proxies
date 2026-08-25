# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 396
- HTTP: 90 alive / 63 gold
- HTTPS: 75 alive / 19 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 159 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37528
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
