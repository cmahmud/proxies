# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 391
- HTTP: 124 alive / 64 gold
- HTTPS: 55 alive / 9 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 189 alive / 161 gold

## Historical pool

- Discovered: 177586
- Ever alive: 33323
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
