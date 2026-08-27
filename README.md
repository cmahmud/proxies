# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 412
- HTTP: 99 alive / 59 gold
- HTTPS: 104 alive / 23 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 199 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41490
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
