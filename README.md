# SyndProxy private pool

## Current pool

- Alive now: 1021
- Gold now: 373
- HTTP: 307 alive / 62 gold
- HTTPS: 238 alive / 16 gold
- SOCKS4: 242 alive / 152 gold
- SOCKS5: 234 alive / 143 gold

## Historical pool

- Discovered: 109322
- Ever alive: 15172
- Ever gold: 488

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
