# SyndProxy validated proxy pool

## Current pool

- Alive now: 683
- Gold now: 347
- HTTP: 134 alive / 37 gold
- HTTPS: 134 alive / 9 gold
- SOCKS4: 194 alive / 153 gold
- SOCKS5: 221 alive / 148 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32878
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
