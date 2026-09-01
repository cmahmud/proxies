# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 441
- HTTP: 111 alive / 81 gold
- HTTPS: 88 alive / 29 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 189 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47013
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
