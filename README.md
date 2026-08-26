# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 374
- HTTP: 98 alive / 58 gold
- HTTPS: 63 alive / 20 gold
- SOCKS4: 156 alive / 142 gold
- SOCKS5: 172 alive / 154 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38851
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
