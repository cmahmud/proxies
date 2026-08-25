# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 399
- HTTP: 93 alive / 54 gold
- HTTPS: 51 alive / 15 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36622
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
