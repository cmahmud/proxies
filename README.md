# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 421
- HTTP: 88 alive / 68 gold
- HTTPS: 77 alive / 27 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 179 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47256
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
