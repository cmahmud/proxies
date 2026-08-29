# SyndProxy validated proxy pool

## Current pool

- Alive now: 414
- Gold now: 360
- HTTP: 51 alive / 38 gold
- HTTPS: 29 alive / 6 gold
- SOCKS4: 163 alive / 157 gold
- SOCKS5: 171 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43556
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
