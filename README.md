# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 426
- HTTP: 102 alive / 77 gold
- HTTPS: 38 alive / 17 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 179 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48977
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
