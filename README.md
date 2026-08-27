# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 400
- HTTP: 107 alive / 62 gold
- HTTPS: 166 alive / 13 gold
- SOCKS4: 182 alive / 160 gold
- SOCKS5: 180 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40908
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
