# SyndProxy private pool

## Current pool

- Alive now: 778
- Gold now: 405
- HTTP: 234 alive / 91 gold
- HTTPS: 152 alive / 27 gold
- SOCKS4: 176 alive / 129 gold
- SOCKS5: 216 alive / 158 gold

## Historical pool

- Discovered: 162701
- Ever alive: 31453
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
