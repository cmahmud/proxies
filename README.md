# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 399
- HTTP: 85 alive / 58 gold
- HTTPS: 37 alive / 16 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 179 alive / 165 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36777
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
