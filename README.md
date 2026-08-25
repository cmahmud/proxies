# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 401
- HTTP: 91 alive / 62 gold
- HTTPS: 50 alive / 16 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36756
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
