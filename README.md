# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 430
- HTTP: 119 alive / 80 gold
- HTTPS: 126 alive / 23 gold
- SOCKS4: 182 alive / 159 gold
- SOCKS5: 192 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42166
- Ever gold: 1352

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
