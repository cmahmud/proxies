# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 399
- HTTP: 86 alive / 57 gold
- HTTPS: 48 alive / 14 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36645
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
