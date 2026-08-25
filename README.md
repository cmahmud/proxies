# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 401
- HTTP: 96 alive / 56 gold
- HTTPS: 55 alive / 18 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 177 alive / 165 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36841
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
