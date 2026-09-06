# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 392
- HTTP: 91 alive / 67 gold
- HTTPS: 30 alive / 14 gold
- SOCKS4: 166 alive / 152 gold
- SOCKS5: 185 alive / 159 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48237
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
