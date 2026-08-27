# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 401
- HTTP: 113 alive / 61 gold
- HTTPS: 121 alive / 15 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 188 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41345
- Ever gold: 1325

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
