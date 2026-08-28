# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 424
- HTTP: 111 alive / 78 gold
- HTTPS: 136 alive / 19 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 190 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42415
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
