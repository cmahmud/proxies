# SyndProxy private pool

## Current pool

- Alive now: 987
- Gold now: 415
- HTTP: 293 alive / 83 gold
- HTTPS: 213 alive / 22 gold
- SOCKS4: 240 alive / 163 gold
- SOCKS5: 241 alive / 147 gold

## Historical pool

- Discovered: 158240
- Ever alive: 30021
- Ever gold: 1139

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
