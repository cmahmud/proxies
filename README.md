# SyndProxy validated proxy pool

## Current pool

- Alive now: 610
- Gold now: 436
- HTTP: 126 alive / 80 gold
- HTTPS: 111 alive / 23 gold
- SOCKS4: 183 alive / 162 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34465
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
