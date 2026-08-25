# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 401
- HTTP: 79 alive / 61 gold
- HTTPS: 50 alive / 13 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 178 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36402
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
