# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 388
- HTTP: 132 alive / 70 gold
- HTTPS: 154 alive / 17 gold
- SOCKS4: 162 alive / 149 gold
- SOCKS5: 176 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40136
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
