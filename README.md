# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 402
- HTTP: 93 alive / 59 gold
- HTTPS: 61 alive / 16 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 182 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36855
- Ever gold: 1281

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
