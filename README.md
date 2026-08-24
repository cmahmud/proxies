# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 431
- HTTP: 126 alive / 77 gold
- HTTPS: 88 alive / 22 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33916
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
