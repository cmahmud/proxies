# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 399
- HTTP: 72 alive / 55 gold
- HTTPS: 62 alive / 17 gold
- SOCKS4: 167 alive / 162 gold
- SOCKS5: 179 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42760
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
