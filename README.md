# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 385
- HTTP: 135 alive / 68 gold
- HTTPS: 167 alive / 19 gold
- SOCKS4: 166 alive / 147 gold
- SOCKS5: 179 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39731
- Ever gold: 1301

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
