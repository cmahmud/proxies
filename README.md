# SyndProxy private pool

## Current pool

- Alive now: 863
- Gold now: 476
- HTTP: 261 alive / 122 gold
- HTTPS: 187 alive / 70 gold
- SOCKS4: 205 alive / 144 gold
- SOCKS5: 210 alive / 140 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16783
- Ever gold: 624

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
