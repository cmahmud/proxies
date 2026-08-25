# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 401
- HTTP: 77 alive / 60 gold
- HTTPS: 63 alive / 12 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36461
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
