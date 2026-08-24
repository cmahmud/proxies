# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 388
- HTTP: 95 alive / 53 gold
- HTTPS: 50 alive / 12 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 181 alive / 163 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33550
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
