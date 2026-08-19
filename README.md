# SyndProxy private pool

## Current pool

- Alive now: 1149
- Gold now: 521
- HTTP: 440 alive / 160 gold
- HTTPS: 261 alive / 86 gold
- SOCKS4: 228 alive / 140 gold
- SOCKS5: 220 alive / 135 gold

## Historical pool

- Discovered: 119875
- Ever alive: 18514
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
