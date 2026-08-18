# SyndProxy private pool

## Current pool

- Alive now: 856
- Gold now: 249
- HTTP: 354 alive / 26 gold
- HTTPS: 104 alive / 2 gold
- SOCKS4: 188 alive / 116 gold
- SOCKS5: 210 alive / 105 gold

## Historical pool

- Discovered: 99104
- Ever alive: 11658
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
