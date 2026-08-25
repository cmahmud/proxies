# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 410
- HTTP: 93 alive / 60 gold
- HTTPS: 67 alive / 18 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 194 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36349
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
