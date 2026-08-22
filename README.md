# SyndProxy private pool

## Current pool

- Alive now: 784
- Gold now: 400
- HTTP: 203 alive / 79 gold
- HTTPS: 156 alive / 28 gold
- SOCKS4: 185 alive / 134 gold
- SOCKS5: 240 alive / 159 gold

## Historical pool

- Discovered: 162241
- Ever alive: 31411
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
