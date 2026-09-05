# SyndProxy validated proxy pool

## Current pool

- Alive now: 378
- Gold now: 295
- HTTP: 104 alive / 77 gold
- HTTPS: 43 alive / 21 gold
- SOCKS4: 78 alive / 66 gold
- SOCKS5: 153 alive / 131 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47879
- Ever gold: 1501

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
