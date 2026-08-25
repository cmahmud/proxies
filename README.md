# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 402
- HTTP: 95 alive / 61 gold
- HTTPS: 49 alive / 13 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36419
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
