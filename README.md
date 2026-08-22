# SyndProxy private pool

## Current pool

- Alive now: 935
- Gold now: 413
- HTTP: 260 alive / 92 gold
- HTTPS: 214 alive / 33 gold
- SOCKS4: 212 alive / 130 gold
- SOCKS5: 249 alive / 158 gold

## Historical pool

- Discovered: 162773
- Ever alive: 31669
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
