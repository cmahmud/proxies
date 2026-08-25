# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 412
- HTTP: 85 alive / 66 gold
- HTTPS: 66 alive / 17 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36381
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
