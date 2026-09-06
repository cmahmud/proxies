# SyndProxy validated proxy pool

## Current pool

- Alive now: 425
- Gold now: 291
- HTTP: 89 alive / 57 gold
- HTTPS: 40 alive / 17 gold
- SOCKS4: 149 alive / 120 gold
- SOCKS5: 147 alive / 97 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48361
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
