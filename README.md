# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 385
- HTTP: 105 alive / 57 gold
- HTTPS: 42 alive / 13 gold
- SOCKS4: 167 alive / 155 gold
- SOCKS5: 182 alive / 160 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33192
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
