# SyndProxy private pool

## Current pool

- Alive now: 1135
- Gold now: 533
- HTTP: 407 alive / 170 gold
- HTTPS: 320 alive / 68 gold
- SOCKS4: 207 alive / 148 gold
- SOCKS5: 201 alive / 147 gold

## Historical pool

- Discovered: 127333
- Ever alive: 19736
- Ever gold: 775

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
