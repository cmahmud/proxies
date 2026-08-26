# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 390
- HTTP: 108 alive / 67 gold
- HTTPS: 85 alive / 18 gold
- SOCKS4: 168 alive / 150 gold
- SOCKS5: 180 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39325
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
