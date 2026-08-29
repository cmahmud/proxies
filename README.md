# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 430
- HTTP: 126 alive / 82 gold
- HTTPS: 61 alive / 27 gold
- SOCKS4: 164 alive / 154 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43659
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
