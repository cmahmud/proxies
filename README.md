# SyndProxy validated proxy pool

## Current pool

- Alive now: 379
- Gold now: 296
- HTTP: 105 alive / 77 gold
- HTTPS: 45 alive / 21 gold
- SOCKS4: 76 alive / 66 gold
- SOCKS5: 153 alive / 132 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47882
- Ever gold: 1501

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
