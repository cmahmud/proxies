# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 402
- HTTP: 82 alive / 55 gold
- HTTPS: 50 alive / 18 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36591
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
