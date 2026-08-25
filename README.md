# SyndProxy validated proxy pool

## Current pool

- Alive now: 458
- Gold now: 398
- HTTP: 73 alive / 55 gold
- HTTPS: 34 alive / 14 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36607
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
