# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 411
- HTTP: 100 alive / 70 gold
- HTTPS: 100 alive / 22 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 178 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41800
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
