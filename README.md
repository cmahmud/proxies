# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 420
- HTTP: 93 alive / 67 gold
- HTTPS: 73 alive / 23 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 182 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36950
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
