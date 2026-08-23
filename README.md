# SyndProxy validated proxy pool

## Current pool

- Alive now: 440
- Gold now: 364
- HTTP: 79 alive / 42 gold
- HTTPS: 23 alive / 11 gold
- SOCKS4: 166 alive / 155 gold
- SOCKS5: 172 alive / 156 gold

## Historical pool

- Discovered: 173751
- Ever alive: 33024
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
