# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 373
- HTTP: 84 alive / 59 gold
- HTTPS: 59 alive / 17 gold
- SOCKS4: 158 alive / 143 gold
- SOCKS5: 170 alive / 154 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38877
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
