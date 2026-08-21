# SyndProxy private pool

## Current pool

- Alive now: 807
- Gold now: 417
- HTTP: 219 alive / 85 gold
- HTTPS: 118 alive / 23 gold
- SOCKS4: 228 alive / 152 gold
- SOCKS5: 242 alive / 157 gold

## Historical pool

- Discovered: 157420
- Ever alive: 29748
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
