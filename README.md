# SyndProxy private pool

## Current pool

- Alive now: 1038
- Gold now: 240
- HTTP: 367 alive / 29 gold
- HTTPS: 175 alive / 8 gold
- SOCKS4: 276 alive / 117 gold
- SOCKS5: 220 alive / 86 gold

## Historical pool

- Discovered: 86712
- Ever alive: 6879
- Ever gold: 320

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
