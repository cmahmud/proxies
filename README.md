# SyndProxy validated proxy pool

## Current pool

- Alive now: 591
- Gold now: 425
- HTTP: 107 alive / 77 gold
- HTTPS: 120 alive / 21 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 198 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42413
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
