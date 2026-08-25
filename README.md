# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 399
- HTTP: 87 alive / 53 gold
- HTTPS: 49 alive / 17 gold
- SOCKS4: 185 alive / 161 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36678
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
