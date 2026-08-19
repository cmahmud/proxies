# SyndProxy private pool

## Current pool

- Alive now: 1037
- Gold now: 515
- HTTP: 357 alive / 161 gold
- HTTPS: 255 alive / 91 gold
- SOCKS4: 217 alive / 143 gold
- SOCKS5: 208 alive / 120 gold

## Historical pool

- Discovered: 119842
- Ever alive: 18369
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
