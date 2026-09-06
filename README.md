# SyndProxy validated proxy pool

## Current pool

- Alive now: 422
- Gold now: 335
- HTTP: 81 alive / 57 gold
- HTTPS: 40 alive / 18 gold
- SOCKS4: 151 alive / 133 gold
- SOCKS5: 150 alive / 127 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48346
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
