# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 400
- HTTP: 78 alive / 57 gold
- HTTPS: 52 alive / 13 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 180 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36500
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
