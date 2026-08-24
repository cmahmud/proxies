# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 390
- HTTP: 125 alive / 64 gold
- HTTPS: 55 alive / 9 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 188 alive / 159 gold

## Historical pool

- Discovered: 177586
- Ever alive: 33322
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
