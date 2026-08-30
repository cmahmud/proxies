# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 432
- HTTP: 97 alive / 74 gold
- HTTPS: 59 alive / 28 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44436
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
