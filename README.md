# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 373
- HTTP: 110 alive / 62 gold
- HTTPS: 67 alive / 20 gold
- SOCKS4: 148 alive / 140 gold
- SOCKS5: 171 alive / 151 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38763
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
