# SyndProxy private pool

## Current pool

- Alive now: 793
- Gold now: 352
- HTTP: 233 alive / 77 gold
- HTTPS: 152 alive / 20 gold
- SOCKS4: 211 alive / 124 gold
- SOCKS5: 197 alive / 131 gold

## Historical pool

- Discovered: 157663
- Ever alive: 29788
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
