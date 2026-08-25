# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 400
- HTTP: 81 alive / 60 gold
- HTTPS: 60 alive / 13 gold
- SOCKS4: 182 alive / 160 gold
- SOCKS5: 178 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36402
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
