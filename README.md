# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 432
- HTTP: 127 alive / 83 gold
- HTTPS: 61 alive / 27 gold
- SOCKS4: 165 alive / 155 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43659
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
