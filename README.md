# SyndProxy validated proxy pool

## Current pool

- Alive now: 425
- Gold now: 339
- HTTP: 87 alive / 60 gold
- HTTPS: 30 alive / 11 gold
- SOCKS4: 148 alive / 137 gold
- SOCKS5: 160 alive / 131 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48392
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
