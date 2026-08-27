# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 401
- HTTP: 118 alive / 63 gold
- HTTPS: 160 alive / 13 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40868
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
