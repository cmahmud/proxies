# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 415
- HTTP: 90 alive / 67 gold
- HTTPS: 65 alive / 19 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 172 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37094
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
