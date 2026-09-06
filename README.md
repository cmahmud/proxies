# SyndProxy validated proxy pool

## Current pool

- Alive now: 413
- Gold now: 323
- HTTP: 77 alive / 56 gold
- HTTPS: 42 alive / 12 gold
- SOCKS4: 145 alive / 132 gold
- SOCKS5: 149 alive / 123 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48337
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
