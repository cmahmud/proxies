# SyndProxy validated proxy pool

## Current pool

- Alive now: 425
- Gold now: 348
- HTTP: 89 alive / 66 gold
- HTTPS: 32 alive / 15 gold
- SOCKS4: 147 alive / 135 gold
- SOCKS5: 157 alive / 132 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48381
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
