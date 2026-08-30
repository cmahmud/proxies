# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 423
- HTTP: 114 alive / 77 gold
- HTTPS: 47 alive / 21 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 190 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44479
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
