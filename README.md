# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 398
- HTTP: 80 alive / 54 gold
- HTTPS: 59 alive / 16 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36617
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
