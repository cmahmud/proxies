# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 395
- HTTP: 96 alive / 58 gold
- HTTPS: 37 alive / 15 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 179 alive / 161 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38973
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
