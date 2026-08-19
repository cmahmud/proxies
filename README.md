# SyndProxy private pool

## Current pool

- Alive now: 1133
- Gold now: 522
- HTTP: 427 alive / 159 gold
- HTTPS: 264 alive / 85 gold
- SOCKS4: 228 alive / 142 gold
- SOCKS5: 214 alive / 136 gold

## Historical pool

- Discovered: 119849
- Ever alive: 18509
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
