# SyndProxy validated proxy pool

## Current pool

- Alive now: 413
- Gold now: 343
- HTTP: 82 alive / 65 gold
- HTTPS: 31 alive / 15 gold
- SOCKS4: 147 alive / 137 gold
- SOCKS5: 153 alive / 126 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48377
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
