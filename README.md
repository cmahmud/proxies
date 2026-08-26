# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 415
- HTTP: 104 alive / 68 gold
- HTTPS: 84 alive / 17 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38005
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
