# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 404
- HTTP: 107 alive / 57 gold
- HTTPS: 53 alive / 19 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 177 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36807
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
