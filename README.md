# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 415
- HTTP: 113 alive / 73 gold
- HTTPS: 84 alive / 16 gold
- SOCKS4: 174 alive / 157 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34877
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
