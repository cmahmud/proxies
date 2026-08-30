# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 432
- HTTP: 106 alive / 76 gold
- HTTPS: 64 alive / 26 gold
- SOCKS4: 164 alive / 162 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44420
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
