# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 452
- HTTP: 126 alive / 84 gold
- HTTPS: 108 alive / 36 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 186 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46978
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
