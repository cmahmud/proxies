# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 353
- HTTP: 122 alive / 80 gold
- HTTPS: 62 alive / 23 gold
- SOCKS4: 127 alive / 105 gold
- SOCKS5: 173 alive / 145 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47979
- Ever gold: 1506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
