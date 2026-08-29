# SyndProxy validated proxy pool

## Current pool

- Alive now: 367
- Gold now: 285
- HTTP: 41 alive / 19 gold
- HTTPS: 5 alive / 0 gold
- SOCKS4: 158 alive / 140 gold
- SOCKS5: 163 alive / 126 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43610
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
