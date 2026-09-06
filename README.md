# SyndProxy validated proxy pool

## Current pool

- Alive now: 425
- Gold now: 327
- HTTP: 84 alive / 62 gold
- HTTPS: 50 alive / 10 gold
- SOCKS4: 145 alive / 133 gold
- SOCKS5: 146 alive / 122 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48369
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
