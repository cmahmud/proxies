# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 415
- HTTP: 102 alive / 64 gold
- HTTPS: 82 alive / 22 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35488
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
