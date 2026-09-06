# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 388
- HTTP: 100 alive / 69 gold
- HTTPS: 35 alive / 16 gold
- SOCKS4: 163 alive / 150 gold
- SOCKS5: 176 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48210
- Ever gold: 1524

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
