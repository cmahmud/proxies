# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 391
- HTTP: 97 alive / 53 gold
- HTTPS: 53 alive / 13 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 179 alive / 164 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33552
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
