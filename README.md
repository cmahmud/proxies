# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 384
- HTTP: 111 alive / 54 gold
- HTTPS: 42 alive / 9 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 183 alive / 162 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33536
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
