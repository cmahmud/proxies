# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 452
- HTTP: 129 alive / 88 gold
- HTTPS: 111 alive / 28 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 189 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46733
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
