# SyndProxy private pool

## Current pool

- Alive now: 743
- Gold now: 374
- HTTP: 181 alive / 70 gold
- HTTPS: 140 alive / 22 gold
- SOCKS4: 189 alive / 119 gold
- SOCKS5: 233 alive / 163 gold

## Historical pool

- Discovered: 148332
- Ever alive: 26076
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
