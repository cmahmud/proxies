# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 425
- HTTP: 141 alive / 82 gold
- HTTPS: 77 alive / 32 gold
- SOCKS4: 160 alive / 151 gold
- SOCKS5: 249 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43915
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
