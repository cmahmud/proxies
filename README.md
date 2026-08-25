# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 401
- HTTP: 86 alive / 54 gold
- HTTPS: 60 alive / 16 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 177 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36595
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
