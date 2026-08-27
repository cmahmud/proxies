# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 420
- HTTP: 101 alive / 78 gold
- HTTPS: 129 alive / 16 gold
- SOCKS4: 185 alive / 159 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42146
- Ever gold: 1351

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
