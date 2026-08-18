# SyndProxy private pool

## Current pool

- Alive now: 847
- Gold now: 221
- HTTP: 270 alive / 33 gold
- HTTPS: 155 alive / 9 gold
- SOCKS4: 216 alive / 111 gold
- SOCKS5: 206 alive / 68 gold

## Historical pool

- Discovered: 94321
- Ever alive: 9327
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
