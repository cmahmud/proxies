# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 373
- HTTP: 114 alive / 63 gold
- HTTPS: 58 alive / 19 gold
- SOCKS4: 150 alive / 139 gold
- SOCKS5: 174 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38775
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
