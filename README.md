# SyndProxy private pool

## Current pool

- Alive now: 859
- Gold now: 367
- HTTP: 289 alive / 73 gold
- HTTPS: 174 alive / 21 gold
- SOCKS4: 187 alive / 128 gold
- SOCKS5: 209 alive / 145 gold

## Historical pool

- Discovered: 157406
- Ever alive: 29670
- Ever gold: 1135

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
