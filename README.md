# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 400
- HTTP: 94 alive / 55 gold
- HTTPS: 55 alive / 14 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36627
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
