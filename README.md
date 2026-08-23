# SyndProxy validated proxy pool

## Current pool

- Alive now: 390
- Gold now: 201
- HTTP: 158 alive / 36 gold
- HTTPS: 31 alive / 7 gold
- SOCKS4: 86 alive / 70 gold
- SOCKS5: 115 alive / 88 gold

## Historical pool

- Discovered: 170566
- Ever alive: 32766
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
