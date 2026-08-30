# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 431
- HTTP: 106 alive / 76 gold
- HTTPS: 50 alive / 25 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 193 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44455
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
