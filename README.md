# SyndProxy private pool

## Current pool

- Alive now: 885
- Gold now: 411
- HTTP: 228 alive / 88 gold
- HTTPS: 198 alive / 20 gold
- SOCKS4: 217 alive / 151 gold
- SOCKS5: 242 alive / 152 gold

## Historical pool

- Discovered: 151674
- Ever alive: 27568
- Ever gold: 1099

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
