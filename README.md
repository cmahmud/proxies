# SyndProxy validated proxy pool

## Current pool

- Alive now: 419
- Gold now: 346
- HTTP: 85 alive / 67 gold
- HTTPS: 30 alive / 16 gold
- SOCKS4: 149 alive / 129 gold
- SOCKS5: 155 alive / 134 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48381
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
