# SyndProxy validated proxy pool

## Current pool

- Alive now: 657
- Gold now: 411
- HTTP: 111 alive / 64 gold
- HTTPS: 170 alive / 17 gold
- SOCKS4: 180 alive / 157 gold
- SOCKS5: 196 alive / 173 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40681
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
