# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 408
- HTTP: 87 alive / 58 gold
- HTTPS: 68 alive / 17 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 193 alive / 172 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36316
- Ever gold: 1272

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
