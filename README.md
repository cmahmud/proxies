# SyndProxy private pool

## Current pool

- Alive now: 1068
- Gold now: 402
- HTTP: 372 alive / 90 gold
- HTTPS: 258 alive / 27 gold
- SOCKS4: 193 alive / 116 gold
- SOCKS5: 245 alive / 169 gold

## Historical pool

- Discovered: 166621
- Ever alive: 32451
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
