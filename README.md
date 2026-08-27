# SyndProxy validated proxy pool

## Current pool

- Alive now: 602
- Gold now: 417
- HTTP: 103 alive / 69 gold
- HTTPS: 133 alive / 18 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41329
- Ever gold: 1325

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
