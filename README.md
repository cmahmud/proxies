# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 343
- HTTP: 147 alive / 39 gold
- HTTPS: 75 alive / 9 gold
- SOCKS4: 175 alive / 153 gold
- SOCKS5: 199 alive / 142 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32878
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
