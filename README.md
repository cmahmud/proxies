# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 435
- HTTP: 106 alive / 79 gold
- HTTPS: 56 alive / 27 gold
- SOCKS4: 165 alive / 162 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44459
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
