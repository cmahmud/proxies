# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 408
- HTTP: 93 alive / 58 gold
- HTTPS: 74 alive / 21 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 176 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36913
- Ever gold: 1281

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
