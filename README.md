# SyndProxy private pool

## Current pool

- Alive now: 984
- Gold now: 420
- HTTP: 342 alive / 86 gold
- HTTPS: 216 alive / 28 gold
- SOCKS4: 198 alive / 141 gold
- SOCKS5: 228 alive / 165 gold

## Historical pool

- Discovered: 163875
- Ever alive: 32026
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
