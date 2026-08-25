# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 409
- HTTP: 87 alive / 58 gold
- HTTPS: 73 alive / 17 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 195 alive / 173 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36316
- Ever gold: 1271

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
