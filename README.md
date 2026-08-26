# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 377
- HTTP: 113 alive / 66 gold
- HTTPS: 62 alive / 20 gold
- SOCKS4: 148 alive / 139 gold
- SOCKS5: 175 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38774
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
