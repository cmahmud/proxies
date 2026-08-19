# SyndProxy private pool

## Current pool

- Alive now: 1139
- Gold now: 531
- HTTP: 420 alive / 155 gold
- HTTPS: 262 alive / 90 gold
- SOCKS4: 238 alive / 150 gold
- SOCKS5: 219 alive / 136 gold

## Historical pool

- Discovered: 119808
- Ever alive: 18017
- Ever gold: 706

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
