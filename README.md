# SyndProxy validated proxy pool

## Current pool

- Alive now: 449
- Gold now: 364
- HTTP: 74 alive / 51 gold
- HTTPS: 30 alive / 8 gold
- SOCKS4: 165 alive / 153 gold
- SOCKS5: 180 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48284
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
