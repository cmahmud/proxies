# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 396
- HTTP: 107 alive / 77 gold
- HTTPS: 40 alive / 17 gold
- SOCKS4: 169 alive / 152 gold
- SOCKS5: 173 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48201
- Ever gold: 1523

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
