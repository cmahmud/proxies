# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 411
- HTTP: 97 alive / 66 gold
- HTTPS: 84 alive / 21 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 172 alive / 162 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37067
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
