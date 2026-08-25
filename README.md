# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 401
- HTTP: 75 alive / 56 gold
- HTTPS: 62 alive / 14 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36487
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
