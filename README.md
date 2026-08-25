# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 410
- HTTP: 89 alive / 69 gold
- HTTPS: 72 alive / 22 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 172 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37137
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
