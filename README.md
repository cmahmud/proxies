# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 406
- HTTP: 96 alive / 63 gold
- HTTPS: 86 alive / 16 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 193 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39254
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
