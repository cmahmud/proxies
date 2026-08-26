# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 403
- HTTP: 108 alive / 57 gold
- HTTPS: 78 alive / 16 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39131
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
