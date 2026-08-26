# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 405
- HTTP: 92 alive / 62 gold
- HTTPS: 70 alive / 19 gold
- SOCKS4: 174 alive / 156 gold
- SOCKS5: 193 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38524
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
