# SyndProxy validated proxy pool

## Current pool

- Alive now: 452
- Gold now: 366
- HTTP: 80 alive / 45 gold
- HTTPS: 32 alive / 13 gold
- SOCKS4: 165 alive / 156 gold
- SOCKS5: 175 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48308
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
