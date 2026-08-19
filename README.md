# SyndProxy private pool

## Current pool

- Alive now: 970
- Gold now: 498
- HTTP: 319 alive / 150 gold
- HTTPS: 226 alive / 90 gold
- SOCKS4: 206 alive / 122 gold
- SOCKS5: 219 alive / 136 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17580
- Ever gold: 690

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
