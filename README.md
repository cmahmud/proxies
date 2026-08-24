# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 388
- HTTP: 110 alive / 55 gold
- HTTPS: 41 alive / 11 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 191 alive / 163 gold

## Historical pool

- Discovered: 178001
- Ever alive: 33357
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
