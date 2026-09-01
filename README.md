# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 427
- HTTP: 110 alive / 68 gold
- HTTPS: 75 alive / 30 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 173 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47055
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
