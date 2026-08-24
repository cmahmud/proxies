# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 393
- HTTP: 112 alive / 68 gold
- HTTPS: 54 alive / 16 gold
- SOCKS4: 167 alive / 156 gold
- SOCKS5: 183 alive / 153 gold

## Historical pool

- Discovered: 176968
- Ever alive: 33260
- Ever gold: 1232

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
