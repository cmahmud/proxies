# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 401
- HTTP: 97 alive / 69 gold
- HTTPS: 67 alive / 18 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 168 alive / 154 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37220
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
