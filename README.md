# SyndProxy validated proxy pool

## Current pool

- Alive now: 415
- Gold now: 193
- HTTP: 154 alive / 40 gold
- HTTPS: 50 alive / 8 gold
- SOCKS4: 89 alive / 64 gold
- SOCKS5: 122 alive / 81 gold

## Historical pool

- Discovered: 170278
- Ever alive: 32719
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
