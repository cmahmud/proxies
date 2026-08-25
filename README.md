# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 398
- HTTP: 91 alive / 54 gold
- HTTPS: 47 alive / 14 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36624
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
