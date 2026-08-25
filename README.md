# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 401
- HTTP: 84 alive / 56 gold
- HTTPS: 49 alive / 16 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36684
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
