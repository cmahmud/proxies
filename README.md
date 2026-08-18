# SyndProxy private pool

## Current pool

- Alive now: 1022
- Gold now: 369
- HTTP: 297 alive / 61 gold
- HTTPS: 242 alive / 14 gold
- SOCKS4: 247 alive / 151 gold
- SOCKS5: 236 alive / 143 gold

## Historical pool

- Discovered: 109322
- Ever alive: 15174
- Ever gold: 488

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
