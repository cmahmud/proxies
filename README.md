# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 399
- HTTP: 76 alive / 52 gold
- HTTPS: 47 alive / 16 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 182 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36574
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
