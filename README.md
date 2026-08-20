# SyndProxy private pool

## Current pool

- Alive now: 770
- Gold now: 360
- HTTP: 223 alive / 83 gold
- HTTPS: 175 alive / 18 gold
- SOCKS4: 198 alive / 144 gold
- SOCKS5: 174 alive / 115 gold

## Historical pool

- Discovered: 145543
- Ever alive: 25333
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
