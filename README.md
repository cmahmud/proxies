# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 392
- HTTP: 77 alive / 53 gold
- HTTPS: 39 alive / 14 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 179 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42844
- Ever gold: 1363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
