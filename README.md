# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 393
- HTTP: 107 alive / 75 gold
- HTTPS: 40 alive / 15 gold
- SOCKS4: 174 alive / 152 gold
- SOCKS5: 172 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48201
- Ever gold: 1523

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
