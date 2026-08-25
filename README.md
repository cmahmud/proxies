# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 401
- HTTP: 87 alive / 55 gold
- HTTPS: 57 alive / 16 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 177 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36594
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
