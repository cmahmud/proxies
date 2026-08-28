# SyndProxy validated proxy pool

## Current pool

- Alive now: 577
- Gold now: 424
- HTTP: 97 alive / 73 gold
- HTTPS: 112 alive / 22 gold
- SOCKS4: 183 alive / 161 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42516
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
