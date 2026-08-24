# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 387
- HTTP: 97 alive / 53 gold
- HTTPS: 52 alive / 12 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 180 alive / 161 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33552
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
