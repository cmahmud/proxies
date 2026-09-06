# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 399
- HTTP: 88 alive / 64 gold
- HTTPS: 34 alive / 16 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 188 alive / 163 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48251
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
