# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 430
- HTTP: 108 alive / 73 gold
- HTTPS: 65 alive / 27 gold
- SOCKS4: 165 alive / 162 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44425
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
