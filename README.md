# SyndProxy private pool

## Current pool

- Alive now: 1266
- Gold now: 415
- HTTP: 436 alive / 90 gold
- HTTPS: 301 alive / 22 gold
- SOCKS4: 237 alive / 142 gold
- SOCKS5: 292 alive / 161 gold

## Historical pool

- Discovered: 136183
- Ever alive: 22303
- Ever gold: 895

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
