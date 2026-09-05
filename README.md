# SyndProxy validated proxy pool

## Current pool

- Alive now: 667
- Gold now: 303
- HTTP: 233 alive / 77 gold
- HTTPS: 39 alive / 22 gold
- SOCKS4: 201 alive / 68 gold
- SOCKS5: 194 alive / 136 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47817
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
