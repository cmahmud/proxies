# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 400
- HTTP: 108 alive / 64 gold
- HTTPS: 82 alive / 19 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 165 alive / 159 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37297
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
