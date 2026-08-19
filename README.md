# SyndProxy private pool

## Current pool

- Alive now: 1148
- Gold now: 602
- HTTP: 450 alive / 192 gold
- HTTPS: 265 alive / 111 gold
- SOCKS4: 214 alive / 144 gold
- SOCKS5: 219 alive / 155 gold

## Historical pool

- Discovered: 124852
- Ever alive: 19417
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
