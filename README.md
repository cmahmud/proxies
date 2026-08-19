# SyndProxy private pool

## Current pool

- Alive now: 1135
- Gold now: 523
- HTTP: 424 alive / 161 gold
- HTTPS: 273 alive / 85 gold
- SOCKS4: 226 alive / 141 gold
- SOCKS5: 212 alive / 136 gold

## Historical pool

- Discovered: 119849
- Ever alive: 18511
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
