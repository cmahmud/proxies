# SyndProxy private pool

## Current pool

- Alive now: 791
- Gold now: 326
- HTTP: 247 alive / 58 gold
- HTTPS: 162 alive / 16 gold
- SOCKS4: 190 alive / 125 gold
- SOCKS5: 192 alive / 127 gold

## Historical pool

- Discovered: 127417
- Ever alive: 19981
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
