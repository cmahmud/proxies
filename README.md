# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 400
- HTTP: 75 alive / 54 gold
- HTTPS: 42 alive / 14 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 182 alive / 172 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36447
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
