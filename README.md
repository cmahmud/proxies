# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 409
- HTTP: 90 alive / 65 gold
- HTTPS: 61 alive / 19 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 177 alive / 165 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36985
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
