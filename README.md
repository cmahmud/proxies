# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 402
- HTTP: 78 alive / 56 gold
- HTTPS: 50 alive / 14 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 180 alive / 172 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36450
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
