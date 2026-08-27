# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 415
- HTTP: 113 alive / 75 gold
- HTTPS: 118 alive / 19 gold
- SOCKS4: 177 alive / 157 gold
- SOCKS5: 191 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42083
- Ever gold: 1349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
