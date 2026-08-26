# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 383
- HTTP: 108 alive / 65 gold
- HTTPS: 48 alive / 18 gold
- SOCKS4: 157 alive / 144 gold
- SOCKS5: 176 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38918
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
