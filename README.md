# SyndProxy private pool

## Current pool

- Alive now: 1208
- Gold now: 415
- HTTP: 427 alive / 101 gold
- HTTPS: 278 alive / 28 gold
- SOCKS4: 225 alive / 131 gold
- SOCKS5: 278 alive / 155 gold

## Historical pool

- Discovered: 152746
- Ever alive: 28116
- Ever gold: 1104

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
