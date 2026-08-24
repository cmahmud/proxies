# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 388
- HTTP: 86 alive / 50 gold
- HTTPS: 46 alive / 12 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33554
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
