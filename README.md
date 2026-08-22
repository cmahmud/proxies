# SyndProxy private pool

## Current pool

- Alive now: 748
- Gold now: 386
- HTTP: 190 alive / 73 gold
- HTTPS: 140 alive / 27 gold
- SOCKS4: 205 alive / 144 gold
- SOCKS5: 213 alive / 142 gold

## Historical pool

- Discovered: 163333
- Ever alive: 31888
- Ever gold: 1168

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
