# SyndProxy private pool

## Current pool

- Alive now: 1231
- Gold now: 565
- HTTP: 445 alive / 186 gold
- HTTPS: 327 alive / 94 gold
- SOCKS4: 205 alive / 127 gold
- SOCKS5: 254 alive / 158 gold

## Historical pool

- Discovered: 138813
- Ever alive: 22944
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
