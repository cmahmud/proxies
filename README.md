# SyndProxy private pool

## Current pool

- Alive now: 1755
- Gold now: 657
- HTTP: 736 alive / 240 gold
- HTTPS: 574 alive / 139 gold
- SOCKS4: 207 alive / 135 gold
- SOCKS5: 238 alive / 143 gold

## Historical pool

- Discovered: 142719
- Ever alive: 24521
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
