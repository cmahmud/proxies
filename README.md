# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 447
- HTTP: 121 alive / 88 gold
- HTTPS: 55 alive / 30 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 177 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43677
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
