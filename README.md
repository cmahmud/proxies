# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 455
- HTTP: 111 alive / 89 gold
- HTTPS: 126 alive / 33 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45654
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
