# SyndProxy private pool

## Current pool

- Alive now: 1118
- Gold now: 439
- HTTP: 359 alive / 108 gold
- HTTPS: 289 alive / 33 gold
- SOCKS4: 204 alive / 143 gold
- SOCKS5: 266 alive / 155 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28648
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
