# SyndProxy private pool

## Current pool

- Alive now: 1761
- Gold now: 643
- HTTP: 698 alive / 216 gold
- HTTPS: 520 alive / 117 gold
- SOCKS4: 227 alive / 148 gold
- SOCKS5: 316 alive / 162 gold

## Historical pool

- Discovered: 142096
- Ever alive: 24223
- Ever gold: 971

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
