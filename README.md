# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 431
- HTTP: 134 alive / 81 gold
- HTTPS: 88 alive / 23 gold
- SOCKS4: 180 alive / 160 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 181494
- Ever alive: 34076
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
