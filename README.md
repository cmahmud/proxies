# SyndProxy private pool

## Current pool

- Alive now: 1039
- Gold now: 561
- HTTP: 340 alive / 187 gold
- HTTPS: 290 alive / 108 gold
- SOCKS4: 186 alive / 120 gold
- SOCKS5: 223 alive / 146 gold

## Historical pool

- Discovered: 124835
- Ever alive: 19202
- Ever gold: 770

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
