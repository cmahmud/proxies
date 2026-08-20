# SyndProxy private pool

## Current pool

- Alive now: 1794
- Gold now: 616
- HTTP: 767 alive / 244 gold
- HTTPS: 592 alive / 116 gold
- SOCKS4: 182 alive / 103 gold
- SOCKS5: 253 alive / 153 gold

## Historical pool

- Discovered: 143486
- Ever alive: 24790
- Ever gold: 1045

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
