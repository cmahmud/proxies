# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 401
- HTTP: 83 alive / 56 gold
- HTTPS: 45 alive / 14 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36607
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
