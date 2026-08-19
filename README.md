# SyndProxy private pool

## Current pool

- Alive now: 947
- Gold now: 518
- HTTP: 302 alive / 156 gold
- HTTPS: 241 alive / 88 gold
- SOCKS4: 211 alive / 141 gold
- SOCKS5: 193 alive / 133 gold

## Historical pool

- Discovered: 119849
- Ever alive: 18472
- Ever gold: 719

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
