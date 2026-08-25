# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 402
- HTTP: 90 alive / 54 gold
- HTTPS: 58 alive / 18 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 186 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36589
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
