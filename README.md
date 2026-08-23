# SyndProxy validated proxy pool

## Current pool

- Alive now: 671
- Gold now: 345
- HTTP: 135 alive / 36 gold
- HTTPS: 121 alive / 8 gold
- SOCKS4: 193 alive / 153 gold
- SOCKS5: 222 alive / 148 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32878
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
