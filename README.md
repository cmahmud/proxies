# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 403
- HTTP: 92 alive / 63 gold
- HTTPS: 73 alive / 14 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 195 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39261
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
