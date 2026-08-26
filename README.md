# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 401
- HTTP: 102 alive / 61 gold
- HTTPS: 90 alive / 14 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 196 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38341
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
