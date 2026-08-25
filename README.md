# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 417
- HTTP: 108 alive / 68 gold
- HTTPS: 64 alive / 21 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 174 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37112
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
