# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 408
- HTTP: 97 alive / 73 gold
- HTTPS: 31 alive / 16 gold
- SOCKS4: 170 alive / 154 gold
- SOCKS5: 185 alive / 165 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48247
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
