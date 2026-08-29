# SyndProxy validated proxy pool

## Current pool

- Alive now: 413
- Gold now: 327
- HTTP: 49 alive / 33 gold
- HTTPS: 34 alive / 3 gold
- SOCKS4: 161 alive / 148 gold
- SOCKS5: 169 alive / 143 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43558
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
