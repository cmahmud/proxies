# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 400
- HTTP: 80 alive / 59 gold
- HTTPS: 60 alive / 12 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36459
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
