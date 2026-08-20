# SyndProxy private pool

## Current pool

- Alive now: 1834
- Gold now: 653
- HTTP: 687 alive / 227 gold
- HTTPS: 594 alive / 120 gold
- SOCKS4: 242 alive / 148 gold
- SOCKS5: 311 alive / 158 gold

## Historical pool

- Discovered: 142696
- Ever alive: 24304
- Ever gold: 982

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
