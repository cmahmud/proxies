# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 408
- HTTP: 102 alive / 63 gold
- HTTPS: 79 alive / 19 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39007
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
