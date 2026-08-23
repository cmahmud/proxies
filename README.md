# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 379
- HTTP: 114 alive / 59 gold
- HTTPS: 35 alive / 11 gold
- SOCKS4: 158 alive / 153 gold
- SOCKS5: 170 alive / 156 gold

## Historical pool

- Discovered: 174348
- Ever alive: 33085
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
