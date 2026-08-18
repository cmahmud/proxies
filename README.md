# SyndProxy private pool

## Current pool

- Alive now: 838
- Gold now: 229
- HTTP: 319 alive / 33 gold
- HTTPS: 147 alive / 8 gold
- SOCKS4: 224 alive / 125 gold
- SOCKS5: 148 alive / 63 gold

## Historical pool

- Discovered: 102861
- Ever alive: 13567
- Ever gold: 426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
