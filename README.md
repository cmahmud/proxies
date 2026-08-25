# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 410
- HTTP: 96 alive / 60 gold
- HTTPS: 39 alive / 18 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36742
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
