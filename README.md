# SyndProxy private pool

## Current pool

- Alive now: 798
- Gold now: 334
- HTTP: 252 alive / 60 gold
- HTTPS: 153 alive / 12 gold
- SOCKS4: 209 alive / 144 gold
- SOCKS5: 184 alive / 118 gold

## Historical pool

- Discovered: 129265
- Ever alive: 20153
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
