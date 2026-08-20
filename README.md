# SyndProxy private pool

## Current pool

- Alive now: 1388
- Gold now: 563
- HTTP: 575 alive / 191 gold
- HTTPS: 367 alive / 96 gold
- SOCKS4: 230 alive / 143 gold
- SOCKS5: 216 alive / 133 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22800
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
