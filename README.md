# SyndProxy validated proxy pool

## Current pool

- Alive now: 413
- Gold now: 348
- HTTP: 106 alive / 77 gold
- HTTPS: 49 alive / 25 gold
- SOCKS4: 80 alive / 76 gold
- SOCKS5: 178 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48676
- Ever gold: 1563

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
