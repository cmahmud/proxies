# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 408
- HTTP: 102 alive / 67 gold
- HTTPS: 77 alive / 19 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 170 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37751
- Ever gold: 1287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
