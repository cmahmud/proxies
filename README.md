# SyndProxy private pool

## Current pool

- Alive now: 1622
- Gold now: 652
- HTTP: 570 alive / 214 gold
- HTTPS: 473 alive / 117 gold
- SOCKS4: 239 alive / 160 gold
- SOCKS5: 340 alive / 161 gold

## Historical pool

- Discovered: 141249
- Ever alive: 24153
- Ever gold: 969

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
