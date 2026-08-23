# SyndProxy validated proxy pool

## Current pool

- Alive now: 444
- Gold now: 371
- HTTP: 69 alive / 37 gold
- HTTPS: 29 alive / 13 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 174 alive / 161 gold

## Historical pool

- Discovered: 172855
- Ever alive: 32986
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
