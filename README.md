# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 401
- HTTP: 91 alive / 55 gold
- HTTPS: 44 alive / 17 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36678
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
