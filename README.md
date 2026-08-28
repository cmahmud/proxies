# SyndProxy validated proxy pool

## Current pool

- Alive now: 590
- Gold now: 431
- HTTP: 111 alive / 78 gold
- HTTPS: 121 alive / 23 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 190 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42457
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
