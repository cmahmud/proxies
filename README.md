# SyndProxy private pool

## Current pool

- Alive now: 806
- Gold now: 405
- HTTP: 217 alive / 88 gold
- HTTPS: 149 alive / 31 gold
- SOCKS4: 212 alive / 132 gold
- SOCKS5: 228 alive / 154 gold

## Historical pool

- Discovered: 163842
- Ever alive: 31932
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
