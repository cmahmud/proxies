# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 388
- HTTP: 113 alive / 55 gold
- HTTPS: 57 alive / 10 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 195 alive / 164 gold

## Historical pool

- Discovered: 178001
- Ever alive: 33358
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
