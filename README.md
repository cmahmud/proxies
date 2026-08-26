# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 404
- HTTP: 99 alive / 59 gold
- HTTPS: 73 alive / 16 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39126
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
