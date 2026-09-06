# SyndProxy validated proxy pool

## Current pool

- Alive now: 424
- Gold now: 351
- HTTP: 67 alive / 53 gold
- HTTPS: 27 alive / 12 gold
- SOCKS4: 160 alive / 141 gold
- SOCKS5: 170 alive / 145 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48254
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
