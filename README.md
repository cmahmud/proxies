# SyndProxy validated proxy pool

## Current pool

- Alive now: 610
- Gold now: 471
- HTTP: 135 alive / 94 gold
- HTTPS: 108 alive / 39 gold
- SOCKS4: 175 alive / 164 gold
- SOCKS5: 192 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46889
- Ever gold: 1456

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
