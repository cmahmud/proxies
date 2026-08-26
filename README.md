# SyndProxy validated proxy pool

## Current pool

- Alive now: 608
- Gold now: 396
- HTTP: 118 alive / 75 gold
- HTTPS: 155 alive / 21 gold
- SOCKS4: 159 alive / 147 gold
- SOCKS5: 176 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40122
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
