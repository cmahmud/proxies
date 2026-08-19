# SyndProxy private pool

## Current pool

- Alive now: 1147
- Gold now: 538
- HTTP: 435 alive / 153 gold
- HTTPS: 301 alive / 105 gold
- SOCKS4: 208 alive / 132 gold
- SOCKS5: 203 alive / 148 gold

## Historical pool

- Discovered: 127351
- Ever alive: 19832
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
