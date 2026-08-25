# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 421
- HTTP: 94 alive / 67 gold
- HTTPS: 84 alive / 23 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 37015
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
