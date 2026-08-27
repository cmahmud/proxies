# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 401
- HTTP: 107 alive / 62 gold
- HTTPS: 170 alive / 13 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 181 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40905
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
