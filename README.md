# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 405
- HTTP: 77 alive / 57 gold
- HTTPS: 56 alive / 18 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41576
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
