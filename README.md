# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 422
- HTTP: 99 alive / 72 gold
- HTTPS: 67 alive / 21 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44419
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
