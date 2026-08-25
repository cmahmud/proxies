# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 415
- HTTP: 90 alive / 59 gold
- HTTPS: 75 alive / 20 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 193 alive / 174 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36199
- Ever gold: 1269

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
