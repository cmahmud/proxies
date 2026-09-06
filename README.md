# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 357
- HTTP: 126 alive / 76 gold
- HTTPS: 64 alive / 23 gold
- SOCKS4: 139 alive / 113 gold
- SOCKS5: 173 alive / 145 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47986
- Ever gold: 1506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
