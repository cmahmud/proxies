# SyndProxy private pool

## Current pool

- Alive now: 883
- Gold now: 411
- HTTP: 249 alive / 90 gold
- HTTPS: 187 alive / 26 gold
- SOCKS4: 196 alive / 136 gold
- SOCKS5: 251 alive / 159 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29063
- Ever gold: 1122

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
