# SyndProxy private pool

## Current pool

- Alive now: 943
- Gold now: 347
- HTTP: 278 alive / 51 gold
- HTTPS: 192 alive / 14 gold
- SOCKS4: 239 alive / 144 gold
- SOCKS5: 234 alive / 138 gold

## Historical pool

- Discovered: 107085
- Ever alive: 14720
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
