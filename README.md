# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 398
- HTTP: 117 alive / 58 gold
- HTTPS: 79 alive / 11 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 194 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38257
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
