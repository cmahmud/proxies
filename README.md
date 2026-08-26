# SyndProxy validated proxy pool

## Current pool

- Alive now: 660
- Gold now: 398
- HTTP: 142 alive / 75 gold
- HTTPS: 174 alive / 25 gold
- SOCKS4: 167 alive / 147 gold
- SOCKS5: 177 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40062
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
