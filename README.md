# SyndProxy validated proxy pool

## Current pool

- Alive now: 413
- Gold now: 334
- HTTP: 83 alive / 61 gold
- HTTPS: 36 alive / 11 gold
- SOCKS4: 146 alive / 136 gold
- SOCKS5: 148 alive / 126 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48374
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
