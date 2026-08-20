# SyndProxy private pool

## Current pool

- Alive now: 769
- Gold now: 360
- HTTP: 190 alive / 71 gold
- HTTPS: 144 alive / 20 gold
- SOCKS4: 221 alive / 145 gold
- SOCKS5: 214 alive / 124 gold

## Historical pool

- Discovered: 145547
- Ever alive: 25390
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
