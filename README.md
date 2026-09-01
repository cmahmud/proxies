# SyndProxy validated proxy pool

## Current pool

- Alive now: 614
- Gold now: 466
- HTTP: 145 alive / 93 gold
- HTTPS: 111 alive / 39 gold
- SOCKS4: 170 alive / 163 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46906
- Ever gold: 1456

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
