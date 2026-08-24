# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 389
- HTTP: 110 alive / 60 gold
- HTTPS: 48 alive / 9 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 188 alive / 161 gold

## Historical pool

- Discovered: 177586
- Ever alive: 33322
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
