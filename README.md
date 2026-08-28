# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 430
- HTTP: 107 alive / 78 gold
- HTTPS: 113 alive / 18 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 188 alive / 173 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42468
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
