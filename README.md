# SyndProxy private pool

## Current pool

- Alive now: 947
- Gold now: 342
- HTTP: 330 alive / 67 gold
- HTTPS: 196 alive / 16 gold
- SOCKS4: 184 alive / 111 gold
- SOCKS5: 237 alive / 148 gold

## Historical pool

- Discovered: 111011
- Ever alive: 16115
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
