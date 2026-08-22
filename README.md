# SyndProxy private pool

## Current pool

- Alive now: 1052
- Gold now: 435
- HTTP: 319 alive / 85 gold
- HTTPS: 235 alive / 29 gold
- SOCKS4: 240 alive / 152 gold
- SOCKS5: 258 alive / 169 gold

## Historical pool

- Discovered: 164960
- Ever alive: 32240
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
