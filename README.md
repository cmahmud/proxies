# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 400
- HTTP: 95 alive / 69 gold
- HTTPS: 65 alive / 18 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 169 alive / 154 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37221
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
