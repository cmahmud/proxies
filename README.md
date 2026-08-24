# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 386
- HTTP: 98 alive / 49 gold
- HTTPS: 53 alive / 12 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 179 alive / 163 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33552
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
