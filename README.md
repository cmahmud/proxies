# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 420
- HTTP: 320 alive / 96 gold
- HTTPS: 241 alive / 24 gold
- SOCKS4: 209 alive / 141 gold
- SOCKS5: 261 alive / 159 gold

## Historical pool

- Discovered: 158911
- Ever alive: 30118
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
