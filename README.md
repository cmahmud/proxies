# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 401
- HTTP: 78 alive / 57 gold
- HTTPS: 45 alive / 14 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 183 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36492
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
