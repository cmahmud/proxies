# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 433
- HTTP: 127 alive / 78 gold
- HTTPS: 88 alive / 26 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34656
- Ever gold: 1257

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
