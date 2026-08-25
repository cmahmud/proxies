# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 401
- HTTP: 85 alive / 57 gold
- HTTPS: 38 alive / 16 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36758
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
