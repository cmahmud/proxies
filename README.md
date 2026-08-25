# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 412
- HTTP: 94 alive / 66 gold
- HTTPS: 67 alive / 17 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 171 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37092
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
