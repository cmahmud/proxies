# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 399
- HTTP: 90 alive / 66 gold
- HTTPS: 78 alive / 18 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 168 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37256
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
