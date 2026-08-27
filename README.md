# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 401
- HTTP: 91 alive / 59 gold
- HTTPS: 59 alive / 19 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 182 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41700
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
