# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 415
- HTTP: 109 alive / 69 gold
- HTTPS: 71 alive / 16 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37992
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
