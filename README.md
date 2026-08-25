# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 419
- HTTP: 107 alive / 62 gold
- HTTPS: 74 alive / 20 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 199 alive / 176 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35996
- Ever gold: 1262

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
