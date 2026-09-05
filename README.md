# SyndProxy validated proxy pool

## Current pool

- Alive now: 468
- Gold now: 343
- HTTP: 115 alive / 81 gold
- HTTPS: 61 alive / 23 gold
- SOCKS4: 122 alive / 97 gold
- SOCKS5: 170 alive / 142 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47970
- Ever gold: 1506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
