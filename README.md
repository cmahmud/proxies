# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 349
- HTTP: 185 alive / 40 gold
- HTTPS: 63 alive / 9 gold
- SOCKS4: 169 alive / 153 gold
- SOCKS5: 184 alive / 147 gold

## Historical pool

- Discovered: 171044
- Ever alive: 32846
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
