# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 433
- HTTP: 102 alive / 77 gold
- HTTPS: 66 alive / 26 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44430
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
