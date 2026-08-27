# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 407
- HTTP: 114 alive / 64 gold
- HTTPS: 169 alive / 13 gold
- SOCKS4: 180 alive / 164 gold
- SOCKS5: 189 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41138
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
