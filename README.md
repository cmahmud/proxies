# SyndProxy private pool

## Current pool

- Alive now: 852
- Gold now: 386
- HTTP: 273 alive / 79 gold
- HTTPS: 158 alive / 33 gold
- SOCKS4: 203 alive / 144 gold
- SOCKS5: 218 alive / 130 gold

## Historical pool

- Discovered: 163327
- Ever alive: 31852
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
