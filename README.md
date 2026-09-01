# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 414
- HTTP: 91 alive / 62 gold
- HTTPS: 41 alive / 21 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 177 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47083
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
