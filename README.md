# SyndProxy private pool

## Current pool

- Alive now: 943
- Gold now: 333
- HTTP: 324 alive / 80 gold
- HTTPS: 223 alive / 30 gold
- SOCKS4: 209 alive / 136 gold
- SOCKS5: 187 alive / 87 gold

## Historical pool

- Discovered: 167104
- Ever alive: 32514
- Ever gold: 1184

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
