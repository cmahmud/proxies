# SyndProxy validated proxy pool

## Current pool

- Alive now: 468
- Gold now: 396
- HTTP: 81 alive / 55 gold
- HTTPS: 38 alive / 18 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 180 alive / 165 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36761
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
