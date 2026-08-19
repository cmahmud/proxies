# SyndProxy private pool

## Current pool

- Alive now: 1117
- Gold now: 422
- HTTP: 359 alive / 89 gold
- HTTPS: 262 alive / 15 gold
- SOCKS4: 254 alive / 155 gold
- SOCKS5: 242 alive / 163 gold

## Historical pool

- Discovered: 131719
- Ever alive: 20754
- Ever gold: 875

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
