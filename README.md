# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 404
- HTTP: 83 alive / 60 gold
- HTTPS: 64 alive / 13 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 184 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36458
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
