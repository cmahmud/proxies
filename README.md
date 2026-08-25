# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 420
- HTTP: 99 alive / 66 gold
- HTTPS: 67 alive / 23 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 178 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36971
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
