# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 404
- HTTP: 100 alive / 59 gold
- HTTPS: 55 alive / 16 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 180 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36784
- Ever gold: 1279

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
