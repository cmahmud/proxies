# SyndProxy private pool

## Current pool

- Alive now: 808
- Gold now: 402
- HTTP: 199 alive / 85 gold
- HTTPS: 153 alive / 28 gold
- SOCKS4: 211 alive / 133 gold
- SOCKS5: 245 alive / 156 gold

## Historical pool

- Discovered: 162771
- Ever alive: 31644
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
