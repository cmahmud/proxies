# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 379
- HTTP: 103 alive / 50 gold
- HTTPS: 48 alive / 9 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 180 alive / 161 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33537
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
