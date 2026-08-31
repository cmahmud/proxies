# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 455
- HTTP: 117 alive / 88 gold
- HTTPS: 119 alive / 34 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45651
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
