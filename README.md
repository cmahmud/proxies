# SyndProxy private pool

## Current pool

- Alive now: 1242
- Gold now: 424
- HTTP: 462 alive / 97 gold
- HTTPS: 314 alive / 27 gold
- SOCKS4: 224 alive / 139 gold
- SOCKS5: 242 alive / 161 gold

## Historical pool

- Discovered: 159281
- Ever alive: 30415
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
