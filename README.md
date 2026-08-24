# SyndProxy validated proxy pool

## Current pool

- Alive now: 467
- Gold now: 386
- HTTP: 91 alive / 61 gold
- HTTPS: 36 alive / 11 gold
- SOCKS4: 165 alive / 156 gold
- SOCKS5: 175 alive / 158 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33438
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
