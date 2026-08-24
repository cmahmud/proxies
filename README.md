# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 436
- HTTP: 121 alive / 81 gold
- HTTPS: 70 alive / 24 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 186 alive / 170 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34226
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
