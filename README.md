# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 433
- HTTP: 127 alive / 82 gold
- HTTPS: 65 alive / 28 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43659
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
