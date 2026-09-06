# SyndProxy validated proxy pool

## Current pool

- Alive now: 410
- Gold now: 322
- HTTP: 80 alive / 57 gold
- HTTPS: 36 alive / 11 gold
- SOCKS4: 147 alive / 134 gold
- SOCKS5: 147 alive / 120 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48348
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
