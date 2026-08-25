# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 405
- HTTP: 111 alive / 58 gold
- HTTPS: 60 alive / 17 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 177 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36787
- Ever gold: 1279

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
