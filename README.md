# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 390
- HTTP: 92 alive / 49 gold
- HTTPS: 42 alive / 12 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33548
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
