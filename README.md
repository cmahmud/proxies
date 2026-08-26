# SyndProxy validated proxy pool

## Current pool

- Alive now: 657
- Gold now: 396
- HTTP: 135 alive / 73 gold
- HTTPS: 179 alive / 23 gold
- SOCKS4: 166 alive / 147 gold
- SOCKS5: 177 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40056
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
