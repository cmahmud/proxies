# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 433
- HTTP: 113 alive / 82 gold
- HTTPS: 55 alive / 31 gold
- SOCKS4: 160 alive / 154 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43656
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
