# SyndProxy private pool

## Current pool

- Alive now: 1047
- Gold now: 430
- HTTP: 337 alive / 87 gold
- HTTPS: 219 alive / 27 gold
- SOCKS4: 231 alive / 154 gold
- SOCKS5: 260 alive / 162 gold

## Historical pool

- Discovered: 163867
- Ever alive: 31996
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
