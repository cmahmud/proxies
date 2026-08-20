# SyndProxy private pool

## Current pool

- Alive now: 777
- Gold now: 420
- HTTP: 184 alive / 82 gold
- HTTPS: 140 alive / 27 gold
- SOCKS4: 228 alive / 152 gold
- SOCKS5: 225 alive / 159 gold

## Historical pool

- Discovered: 151059
- Ever alive: 27309
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
