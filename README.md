# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 405
- HTTP: 106 alive / 59 gold
- HTTPS: 52 alive / 17 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 180 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36789
- Ever gold: 1279

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
