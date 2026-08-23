# SyndProxy validated proxy pool

## Current pool

- Alive now: 439
- Gold now: 362
- HTTP: 79 alive / 42 gold
- HTTPS: 23 alive / 11 gold
- SOCKS4: 165 alive / 155 gold
- SOCKS5: 172 alive / 154 gold

## Historical pool

- Discovered: 173751
- Ever alive: 33024
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
