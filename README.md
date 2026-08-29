# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 390
- HTTP: 94 alive / 63 gold
- HTTPS: 75 alive / 15 gold
- SOCKS4: 159 alive / 153 gold
- SOCKS5: 180 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43291
- Ever gold: 1369

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
