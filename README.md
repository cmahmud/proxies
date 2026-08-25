# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 404
- HTTP: 106 alive / 58 gold
- HTTPS: 52 alive / 18 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 178 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36807
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
