# SyndProxy private pool

## Current pool

- Alive now: 1066
- Gold now: 558
- HTTP: 357 alive / 185 gold
- HTTPS: 291 alive / 108 gold
- SOCKS4: 194 alive / 120 gold
- SOCKS5: 224 alive / 145 gold

## Historical pool

- Discovered: 124835
- Ever alive: 19202
- Ever gold: 770

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
