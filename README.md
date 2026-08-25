# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 407
- HTTP: 96 alive / 61 gold
- HTTPS: 58 alive / 16 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36783
- Ever gold: 1279

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
