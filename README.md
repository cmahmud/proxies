# SyndProxy private pool

## Current pool

- Alive now: 728
- Gold now: 385
- HTTP: 194 alive / 62 gold
- HTTPS: 129 alive / 19 gold
- SOCKS4: 197 alive / 150 gold
- SOCKS5: 208 alive / 154 gold

## Historical pool

- Discovered: 146668
- Ever alive: 25755
- Ever gold: 1075

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
