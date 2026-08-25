# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 401
- HTTP: 89 alive / 57 gold
- HTTPS: 58 alive / 17 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36869
- Ever gold: 1281

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
