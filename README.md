# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 401
- HTTP: 104 alive / 70 gold
- HTTPS: 82 alive / 19 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 167 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37437
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
