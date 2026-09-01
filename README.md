# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 425
- HTTP: 117 alive / 69 gold
- HTTPS: 76 alive / 28 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 176 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47055
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
