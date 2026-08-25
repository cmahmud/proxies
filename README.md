# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 411
- HTTP: 84 alive / 65 gold
- HTTPS: 62 alive / 17 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36382
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
