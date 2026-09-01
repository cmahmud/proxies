# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 420
- HTTP: 93 alive / 68 gold
- HTTPS: 51 alive / 24 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 176 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47035
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
