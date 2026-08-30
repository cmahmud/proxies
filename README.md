# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 468
- HTTP: 133 alive / 96 gold
- HTTPS: 128 alive / 39 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 192 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44841
- Ever gold: 1415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
