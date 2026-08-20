# SyndProxy private pool

## Current pool

- Alive now: 784
- Gold now: 389
- HTTP: 203 alive / 82 gold
- HTTPS: 167 alive / 20 gold
- SOCKS4: 201 alive / 135 gold
- SOCKS5: 213 alive / 152 gold

## Historical pool

- Discovered: 151050
- Ever alive: 27180
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
