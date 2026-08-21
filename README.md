# SyndProxy private pool

## Current pool

- Alive now: 1025
- Gold now: 420
- HTTP: 371 alive / 92 gold
- HTTPS: 200 alive / 26 gold
- SOCKS4: 212 alive / 152 gold
- SOCKS5: 242 alive / 150 gold

## Historical pool

- Discovered: 158253
- Ever alive: 30084
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
