# SyndProxy private pool

## Current pool

- Alive now: 945
- Gold now: 397
- HTTP: 278 alive / 86 gold
- HTTPS: 205 alive / 28 gold
- SOCKS4: 220 alive / 137 gold
- SOCKS5: 242 alive / 146 gold

## Historical pool

- Discovered: 163863
- Ever alive: 31974
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
