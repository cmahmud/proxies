# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 405
- HTTP: 96 alive / 62 gold
- HTTPS: 80 alive / 14 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 192 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39228
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
