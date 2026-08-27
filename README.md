# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 411
- HTTP: 102 alive / 64 gold
- HTTPS: 129 alive / 19 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41329
- Ever gold: 1325

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
