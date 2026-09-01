# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 413
- HTTP: 82 alive / 64 gold
- HTTPS: 100 alive / 25 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 178 alive / 166 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47227
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
