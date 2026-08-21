# SyndProxy private pool

## Current pool

- Alive now: 836
- Gold now: 398
- HTTP: 241 alive / 88 gold
- HTTPS: 169 alive / 19 gold
- SOCKS4: 198 alive / 133 gold
- SOCKS5: 228 alive / 158 gold

## Historical pool

- Discovered: 151681
- Ever alive: 27659
- Ever gold: 1102

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
