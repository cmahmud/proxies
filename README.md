# SyndProxy private pool

## Current pool

- Alive now: 870
- Gold now: 283
- HTTP: 236 alive / 25 gold
- HTTPS: 165 alive / 4 gold
- SOCKS4: 240 alive / 142 gold
- SOCKS5: 229 alive / 112 gold

## Historical pool

- Discovered: 99165
- Ever alive: 12345
- Ever gold: 396

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
