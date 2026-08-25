# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 398
- HTTP: 87 alive / 54 gold
- HTTPS: 50 alive / 15 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36638
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
