# SyndProxy validated proxy pool

## Current pool

- Alive now: 408
- Gold now: 280
- HTTP: 82 alive / 54 gold
- HTTPS: 31 alive / 4 gold
- SOCKS4: 146 alive / 117 gold
- SOCKS5: 149 alive / 105 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48371
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
