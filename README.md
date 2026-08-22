# SyndProxy private pool

## Current pool

- Alive now: 813
- Gold now: 415
- HTTP: 235 alive / 85 gold
- HTTPS: 152 alive / 32 gold
- SOCKS4: 196 alive / 147 gold
- SOCKS5: 230 alive / 151 gold

## Historical pool

- Discovered: 163327
- Ever alive: 31852
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
