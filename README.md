# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 422
- HTTP: 111 alive / 63 gold
- HTTPS: 91 alive / 25 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 199 alive / 174 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35776
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
