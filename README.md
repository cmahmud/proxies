# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 401
- HTTP: 97 alive / 55 gold
- HTTPS: 52 alive / 18 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 178 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36843
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
