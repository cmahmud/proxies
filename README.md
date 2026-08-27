# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 396
- HTTP: 93 alive / 56 gold
- HTTPS: 109 alive / 13 gold
- SOCKS4: 183 alive / 167 gold
- SOCKS5: 190 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41523
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
