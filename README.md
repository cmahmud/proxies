# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 389
- HTTP: 135 alive / 71 gold
- HTTPS: 182 alive / 20 gold
- SOCKS4: 158 alive / 145 gold
- SOCKS5: 176 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39996
- Ever gold: 1305

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
