# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 409
- HTTP: 87 alive / 63 gold
- HTTPS: 66 alive / 17 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 195 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36376
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
