# SyndProxy private pool

## Current pool

- Alive now: 1194
- Gold now: 516
- HTTP: 440 alive / 183 gold
- HTTPS: 321 alive / 53 gold
- SOCKS4: 193 alive / 121 gold
- SOCKS5: 240 alive / 159 gold

## Historical pool

- Discovered: 125606
- Ever alive: 19589
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
