# SyndProxy private pool

## Current pool

- Alive now: 830
- Gold now: 415
- HTTP: 230 alive / 77 gold
- HTTPS: 159 alive / 23 gold
- SOCKS4: 221 alive / 154 gold
- SOCKS5: 220 alive / 161 gold

## Historical pool

- Discovered: 151067
- Ever alive: 27391
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
