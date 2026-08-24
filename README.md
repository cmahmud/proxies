# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 431
- HTTP: 116 alive / 80 gold
- HTTPS: 94 alive / 23 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 181494
- Ever alive: 34020
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
