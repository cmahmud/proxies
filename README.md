# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 399
- HTTP: 87 alive / 54 gold
- HTTPS: 52 alive / 14 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36627
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
