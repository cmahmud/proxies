# SyndProxy private pool

## Current pool

- Alive now: 776
- Gold now: 394
- HTTP: 201 alive / 90 gold
- HTTPS: 155 alive / 26 gold
- SOCKS4: 193 alive / 127 gold
- SOCKS5: 227 alive / 151 gold

## Historical pool

- Discovered: 162003
- Ever alive: 31384
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
