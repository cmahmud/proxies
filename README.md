# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 398
- HTTP: 80 alive / 57 gold
- HTTPS: 48 alive / 13 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36501
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
