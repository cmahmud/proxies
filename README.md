# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 417
- HTTP: 89 alive / 67 gold
- HTTPS: 87 alive / 24 gold
- SOCKS4: 168 alive / 157 gold
- SOCKS5: 179 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47250
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
