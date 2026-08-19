# SyndProxy private pool

## Current pool

- Alive now: 1053
- Gold now: 545
- HTTP: 383 alive / 167 gold
- HTTPS: 240 alive / 91 gold
- SOCKS4: 219 alive / 145 gold
- SOCKS5: 211 alive / 142 gold

## Historical pool

- Discovered: 123166
- Ever alive: 18787
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
