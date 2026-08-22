# SyndProxy private pool

## Current pool

- Alive now: 776
- Gold now: 363
- HTTP: 223 alive / 87 gold
- HTTPS: 144 alive / 26 gold
- SOCKS4: 185 alive / 117 gold
- SOCKS5: 224 alive / 133 gold

## Historical pool

- Discovered: 167410
- Ever alive: 32570
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
