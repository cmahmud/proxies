# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 377
- HTTP: 94 alive / 64 gold
- HTTPS: 56 alive / 16 gold
- SOCKS4: 151 alive / 144 gold
- SOCKS5: 170 alive / 153 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38901
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
