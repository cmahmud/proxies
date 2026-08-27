# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 414
- HTTP: 102 alive / 75 gold
- HTTPS: 93 alive / 21 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 181 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41838
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
