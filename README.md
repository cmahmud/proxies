# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 415
- HTTP: 335 alive / 106 gold
- HTTPS: 245 alive / 28 gold
- SOCKS4: 221 alive / 139 gold
- SOCKS5: 242 alive / 142 gold

## Historical pool

- Discovered: 160253
- Ever alive: 30686
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
