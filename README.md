# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 414
- HTTP: 102 alive / 70 gold
- HTTPS: 78 alive / 19 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37124
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
