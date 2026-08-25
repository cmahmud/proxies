# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 394
- HTTP: 89 alive / 65 gold
- HTTPS: 62 alive / 15 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 167 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37269
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
