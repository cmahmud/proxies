# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 423
- HTTP: 113 alive / 69 gold
- HTTPS: 67 alive / 23 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44407
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
