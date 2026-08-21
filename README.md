# SyndProxy private pool

## Current pool

- Alive now: 1302
- Gold now: 422
- HTTP: 502 alive / 104 gold
- HTTPS: 314 alive / 32 gold
- SOCKS4: 231 alive / 154 gold
- SOCKS5: 255 alive / 132 gold

## Historical pool

- Discovered: 159264
- Ever alive: 30345
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
