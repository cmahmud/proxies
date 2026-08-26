# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 408
- HTTP: 105 alive / 63 gold
- HTTPS: 76 alive / 19 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39007
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
