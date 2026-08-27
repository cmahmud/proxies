# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 415
- HTTP: 99 alive / 71 gold
- HTTPS: 101 alive / 24 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 179 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41814
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
