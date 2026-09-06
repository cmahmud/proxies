# SyndProxy validated proxy pool

## Current pool

- Alive now: 419
- Gold now: 348
- HTTP: 84 alive / 63 gold
- HTTPS: 26 alive / 15 gold
- SOCKS4: 150 alive / 137 gold
- SOCKS5: 159 alive / 133 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48396
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
