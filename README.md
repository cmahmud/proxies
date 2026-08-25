# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 405
- HTTP: 106 alive / 58 gold
- HTTPS: 56 alive / 17 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 176 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36787
- Ever gold: 1279

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
