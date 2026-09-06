# SyndProxy validated proxy pool

## Current pool

- Alive now: 413
- Gold now: 328
- HTTP: 79 alive / 61 gold
- HTTPS: 39 alive / 10 gold
- SOCKS4: 149 alive / 136 gold
- SOCKS5: 146 alive / 121 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48354
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
