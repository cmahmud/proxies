# SyndProxy private pool

## Current pool

- Alive now: 766
- Gold now: 418
- HTTP: 185 alive / 86 gold
- HTTPS: 140 alive / 25 gold
- SOCKS4: 213 alive / 142 gold
- SOCKS5: 228 alive / 165 gold

## Historical pool

- Discovered: 151059
- Ever alive: 27302
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
