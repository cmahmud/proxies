# SyndProxy private pool

## Current pool

- Alive now: 1666
- Gold now: 554
- HTTP: 719 alive / 193 gold
- HTTPS: 532 alive / 95 gold
- SOCKS4: 176 alive / 104 gold
- SOCKS5: 239 alive / 162 gold

## Historical pool

- Discovered: 143486
- Ever alive: 24757
- Ever gold: 1037

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
