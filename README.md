# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 401
- HTTP: 102 alive / 55 gold
- HTTPS: 76 alive / 16 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39133
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
