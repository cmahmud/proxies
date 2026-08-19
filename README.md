# SyndProxy private pool

## Current pool

- Alive now: 1055
- Gold now: 402
- HTTP: 312 alive / 77 gold
- HTTPS: 240 alive / 14 gold
- SOCKS4: 256 alive / 151 gold
- SOCKS5: 247 alive / 160 gold

## Historical pool

- Discovered: 131115
- Ever alive: 20544
- Ever gold: 868

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
