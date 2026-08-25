# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 407
- HTTP: 100 alive / 59 gold
- HTTPS: 85 alive / 20 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 176 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36910
- Ever gold: 1281

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
