# SyndProxy validated proxy pool

## Current pool

- Alive now: 587
- Gold now: 410
- HTTP: 118 alive / 64 gold
- HTTPS: 99 alive / 17 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 190 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39305
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
