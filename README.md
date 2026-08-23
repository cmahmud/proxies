# SyndProxy validated proxy pool

## Current pool

- Alive now: 459
- Gold now: 368
- HTTP: 78 alive / 51 gold
- HTTPS: 44 alive / 10 gold
- SOCKS4: 168 alive / 153 gold
- SOCKS5: 169 alive / 154 gold

## Historical pool

- Discovered: 174122
- Ever alive: 33047
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
