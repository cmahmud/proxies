# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 391
- HTTP: 90 alive / 48 gold
- HTTPS: 43 alive / 13 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33548
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
