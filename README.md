# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 343
- HTTP: 126 alive / 39 gold
- HTTPS: 91 alive / 8 gold
- SOCKS4: 181 alive / 152 gold
- SOCKS5: 203 alive / 144 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32878
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
