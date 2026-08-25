# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 410
- HTTP: 114 alive / 72 gold
- HTTPS: 85 alive / 21 gold
- SOCKS4: 162 alive / 158 gold
- SOCKS5: 168 alive / 159 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37182
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
