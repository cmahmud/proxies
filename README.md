# SyndProxy private pool

## Current pool

- Alive now: 921
- Gold now: 370
- HTTP: 277 alive / 84 gold
- HTTPS: 220 alive / 28 gold
- SOCKS4: 193 alive / 122 gold
- SOCKS5: 231 alive / 136 gold

## Historical pool

- Discovered: 153751
- Ever alive: 28845
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
