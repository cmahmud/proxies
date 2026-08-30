# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 424
- HTTP: 107 alive / 72 gold
- HTTPS: 55 alive / 25 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 201 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44470
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
