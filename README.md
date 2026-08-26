# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 405
- HTTP: 91 alive / 62 gold
- HTTPS: 67 alive / 17 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39083
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
