# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 417
- HTTP: 95 alive / 66 gold
- HTTPS: 61 alive / 21 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 177 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36973
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
