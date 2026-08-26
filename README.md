# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 390
- HTTP: 136 alive / 71 gold
- HTTPS: 159 alive / 17 gold
- SOCKS4: 163 alive / 149 gold
- SOCKS5: 182 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40136
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
