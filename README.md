# SyndProxy private pool

## Current pool

- Alive now: 947
- Gold now: 414
- HTTP: 301 alive / 84 gold
- HTTPS: 201 alive / 26 gold
- SOCKS4: 190 alive / 133 gold
- SOCKS5: 255 alive / 171 gold

## Historical pool

- Discovered: 162742
- Ever alive: 31475
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
