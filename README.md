# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 418
- HTTP: 93 alive / 66 gold
- HTTPS: 69 alive / 23 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36949
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
