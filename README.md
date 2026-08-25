# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 408
- HTTP: 92 alive / 69 gold
- HTTPS: 78 alive / 21 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 173 alive / 159 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37140
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
