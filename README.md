# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 415
- HTTP: 95 alive / 61 gold
- HTTPS: 71 alive / 20 gold
- SOCKS4: 186 alive / 162 gold
- SOCKS5: 192 alive / 172 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36230
- Ever gold: 1270

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
