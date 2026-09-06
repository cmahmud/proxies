# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 391
- HTTP: 105 alive / 70 gold
- HTTPS: 36 alive / 16 gold
- SOCKS4: 162 alive / 150 gold
- SOCKS5: 176 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48210
- Ever gold: 1524

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
