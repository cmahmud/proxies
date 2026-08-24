# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 435
- HTTP: 134 alive / 80 gold
- HTTPS: 108 alive / 25 gold
- SOCKS4: 183 alive / 161 gold
- SOCKS5: 194 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34560
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
