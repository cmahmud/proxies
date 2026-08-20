# SyndProxy private pool

## Current pool

- Alive now: 693
- Gold now: 380
- HTTP: 175 alive / 65 gold
- HTTPS: 102 alive / 15 gold
- SOCKS4: 207 alive / 147 gold
- SOCKS5: 209 alive / 153 gold

## Historical pool

- Discovered: 146602
- Ever alive: 25691
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
