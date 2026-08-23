# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 348
- HTTP: 126 alive / 38 gold
- HTTPS: 115 alive / 9 gold
- SOCKS4: 188 alive / 153 gold
- SOCKS5: 217 alive / 148 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32878
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
