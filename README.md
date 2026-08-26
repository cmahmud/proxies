# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 383
- HTTP: 107 alive / 64 gold
- HTTPS: 59 alive / 19 gold
- SOCKS4: 153 alive / 145 gold
- SOCKS5: 174 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38914
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
