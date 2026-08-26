# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 385
- HTTP: 103 alive / 59 gold
- HTTPS: 50 alive / 18 gold
- SOCKS4: 156 alive / 151 gold
- SOCKS5: 180 alive / 157 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38931
- Ever gold: 1294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
