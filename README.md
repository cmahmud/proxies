# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 413
- HTTP: 79 alive / 57 gold
- HTTPS: 42 alive / 21 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 184 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47113
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
