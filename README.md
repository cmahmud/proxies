# SyndProxy private pool

## Current pool

- Alive now: 915
- Gold now: 415
- HTTP: 254 alive / 93 gold
- HTTPS: 209 alive / 32 gold
- SOCKS4: 206 alive / 131 gold
- SOCKS5: 246 alive / 159 gold

## Historical pool

- Discovered: 162773
- Ever alive: 31665
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
