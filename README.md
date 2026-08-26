# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 397
- HTTP: 93 alive / 59 gold
- HTTPS: 34 alive / 15 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 179 alive / 162 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38973
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
