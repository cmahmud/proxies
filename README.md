# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 374
- HTTP: 100 alive / 62 gold
- HTTPS: 67 alive / 15 gold
- SOCKS4: 154 alive / 144 gold
- SOCKS5: 168 alive / 153 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38899
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
