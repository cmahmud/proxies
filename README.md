# SyndProxy private pool

## Current pool

- Alive now: 817
- Gold now: 415
- HTTP: 213 alive / 82 gold
- HTTPS: 143 alive / 27 gold
- SOCKS4: 207 alive / 133 gold
- SOCKS5: 254 alive / 173 gold

## Historical pool

- Discovered: 162742
- Ever alive: 31498
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
