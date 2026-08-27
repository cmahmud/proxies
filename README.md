# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 410
- HTTP: 102 alive / 69 gold
- HTTPS: 99 alive / 19 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 185 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41948
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
