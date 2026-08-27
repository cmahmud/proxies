# SyndProxy validated proxy pool

## Current pool

- Alive now: 586
- Gold now: 409
- HTTP: 99 alive / 60 gold
- HTTPS: 112 alive / 19 gold
- SOCKS4: 180 alive / 167 gold
- SOCKS5: 195 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41519
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
