# SyndProxy private pool

## Current pool

- Alive now: 1729
- Gold now: 612
- HTTP: 765 alive / 205 gold
- HTTPS: 550 alive / 143 gold
- SOCKS4: 180 alive / 101 gold
- SOCKS5: 234 alive / 163 gold

## Historical pool

- Discovered: 143428
- Ever alive: 24713
- Ever gold: 1032

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
