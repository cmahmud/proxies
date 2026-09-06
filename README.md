# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 388
- HTTP: 102 alive / 68 gold
- HTTPS: 41 alive / 13 gold
- SOCKS4: 174 alive / 153 gold
- SOCKS5: 179 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48108
- Ever gold: 1519

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
