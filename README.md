# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 401
- HTTP: 86 alive / 58 gold
- HTTPS: 38 alive / 17 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 180 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36757
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
