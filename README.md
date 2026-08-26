# SyndProxy validated proxy pool

## Current pool

- Alive now: 668
- Gold now: 395
- HTTP: 145 alive / 73 gold
- HTTPS: 180 alive / 22 gold
- SOCKS4: 167 alive / 147 gold
- SOCKS5: 176 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40053
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
