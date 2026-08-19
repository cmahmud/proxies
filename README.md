# SyndProxy private pool

## Current pool

- Alive now: 1213
- Gold now: 500
- HTTP: 394 alive / 122 gold
- HTTPS: 269 alive / 73 gold
- SOCKS4: 255 alive / 154 gold
- SOCKS5: 295 alive / 151 gold

## Historical pool

- Discovered: 114412
- Ever alive: 17030
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
