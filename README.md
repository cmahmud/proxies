# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 399
- HTTP: 76 alive / 57 gold
- HTTPS: 72 alive / 17 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 179 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42756
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
