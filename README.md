# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 399
- HTTP: 122 alive / 75 gold
- HTTPS: 165 alive / 27 gold
- SOCKS4: 165 alive / 148 gold
- SOCKS5: 170 alive / 149 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40104
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
