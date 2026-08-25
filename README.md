# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 403
- HTTP: 94 alive / 60 gold
- HTTPS: 67 alive / 16 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 183 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36858
- Ever gold: 1281

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
