# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 386
- HTTP: 111 alive / 53 gold
- HTTPS: 36 alive / 10 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33536
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
