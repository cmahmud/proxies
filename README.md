# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 386
- HTTP: 98 alive / 51 gold
- HTTPS: 48 alive / 12 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 180 alive / 162 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33552
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
