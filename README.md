# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 387
- HTTP: 92 alive / 61 gold
- HTTPS: 28 alive / 14 gold
- SOCKS4: 169 alive / 152 gold
- SOCKS5: 184 alive / 160 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48241
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
