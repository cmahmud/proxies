# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 407
- HTTP: 109 alive / 67 gold
- HTTPS: 83 alive / 19 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 174 alive / 162 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37746
- Ever gold: 1287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
