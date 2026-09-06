# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 396
- HTTP: 97 alive / 69 gold
- HTTPS: 32 alive / 14 gold
- SOCKS4: 177 alive / 152 gold
- SOCKS5: 186 alive / 161 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48245
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
