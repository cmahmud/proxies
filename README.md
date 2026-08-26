# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 401
- HTTP: 93 alive / 57 gold
- HTTPS: 33 alive / 16 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38976
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
