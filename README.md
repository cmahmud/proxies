# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 405
- HTTP: 93 alive / 60 gold
- HTTPS: 54 alive / 18 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36874
- Ever gold: 1281

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
