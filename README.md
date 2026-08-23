# SyndProxy validated proxy pool

## Current pool

- Alive now: 435
- Gold now: 364
- HTTP: 69 alive / 43 gold
- HTTPS: 26 alive / 10 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 172 alive / 155 gold

## Historical pool

- Discovered: 173751
- Ever alive: 33024
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
