# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 396
- HTTP: 131 alive / 82 gold
- HTTPS: 53 alive / 22 gold
- SOCKS4: 155 alive / 138 gold
- SOCKS5: 185 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48027
- Ever gold: 1512

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
