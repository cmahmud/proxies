# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 400
- HTTP: 92 alive / 58 gold
- HTTPS: 56 alive / 16 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 182 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36854
- Ever gold: 1281

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
