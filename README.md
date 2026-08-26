# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 408
- HTTP: 90 alive / 60 gold
- HTTPS: 71 alive / 19 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 190 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39091
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
