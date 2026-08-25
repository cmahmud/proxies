# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 401
- HTTP: 77 alive / 57 gold
- HTTPS: 42 alive / 14 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 180 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36495
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
