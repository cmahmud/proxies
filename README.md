# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 383
- HTTP: 110 alive / 58 gold
- HTTPS: 46 alive / 11 gold
- SOCKS4: 174 alive / 154 gold
- SOCKS5: 201 alive / 160 gold

## Historical pool

- Discovered: 174830
- Ever alive: 33108
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
