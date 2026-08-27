# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 415
- HTTP: 118 alive / 77 gold
- HTTPS: 114 alive / 16 gold
- SOCKS4: 175 alive / 158 gold
- SOCKS5: 189 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42086
- Ever gold: 1349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
