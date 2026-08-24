# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 376
- HTTP: 98 alive / 48 gold
- HTTPS: 48 alive / 9 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 180 alive / 160 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33537
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
