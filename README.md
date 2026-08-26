# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 415
- HTTP: 104 alive / 67 gold
- HTTPS: 79 alive / 22 gold
- SOCKS4: 169 alive / 163 gold
- SOCKS5: 173 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37765
- Ever gold: 1287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
