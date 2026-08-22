# SyndProxy private pool

## Current pool

- Alive now: 860
- Gold now: 399
- HTTP: 234 alive / 88 gold
- HTTPS: 164 alive / 23 gold
- SOCKS4: 222 alive / 134 gold
- SOCKS5: 240 alive / 154 gold

## Historical pool

- Discovered: 162771
- Ever alive: 31654
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
