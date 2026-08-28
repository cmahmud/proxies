# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 399
- HTTP: 101 alive / 61 gold
- HTTPS: 99 alive / 16 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 179 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43013
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
