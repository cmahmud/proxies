# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 401
- HTTP: 99 alive / 62 gold
- HTTPS: 78 alive / 14 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 193 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39213
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
