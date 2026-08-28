# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 431
- HTTP: 112 alive / 84 gold
- HTTPS: 147 alive / 20 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 197 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42252
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
