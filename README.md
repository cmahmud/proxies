# SyndProxy validated proxy pool

## Current pool

- Alive now: 422
- Gold now: 352
- HTTP: 84 alive / 65 gold
- HTTPS: 27 alive / 15 gold
- SOCKS4: 150 alive / 137 gold
- SOCKS5: 161 alive / 135 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48396
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
