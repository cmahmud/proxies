# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 412
- HTTP: 97 alive / 67 gold
- HTTPS: 102 alive / 15 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42577
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
