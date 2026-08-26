# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 379
- HTTP: 105 alive / 61 gold
- HTTPS: 58 alive / 19 gold
- SOCKS4: 151 alive / 144 gold
- SOCKS5: 175 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38912
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
