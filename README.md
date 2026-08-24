# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 391
- HTTP: 96 alive / 52 gold
- HTTPS: 40 alive / 13 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33550
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
