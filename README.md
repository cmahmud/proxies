# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 408
- HTTP: 100 alive / 67 gold
- HTTPS: 81 alive / 19 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 173 alive / 161 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37735
- Ever gold: 1287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
