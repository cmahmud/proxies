# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 399
- HTTP: 75 alive / 55 gold
- HTTPS: 55 alive / 22 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 182 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42797
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
