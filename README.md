# SyndProxy private pool

## Current pool

- Alive now: 916
- Gold now: 410
- HTTP: 266 alive / 79 gold
- HTTPS: 189 alive / 29 gold
- SOCKS4: 219 alive / 155 gold
- SOCKS5: 242 alive / 147 gold

## Historical pool

- Discovered: 165846
- Ever alive: 32375
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
