# SyndProxy private pool

## Current pool

- Alive now: 1696
- Gold now: 645
- HTTP: 659 alive / 217 gold
- HTTPS: 501 alive / 117 gold
- SOCKS4: 219 alive / 148 gold
- SOCKS5: 317 alive / 163 gold

## Historical pool

- Discovered: 142096
- Ever alive: 24221
- Ever gold: 971

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
