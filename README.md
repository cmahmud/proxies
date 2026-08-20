# SyndProxy private pool

## Current pool

- Alive now: 713
- Gold now: 378
- HTTP: 198 alive / 71 gold
- HTTPS: 119 alive / 18 gold
- SOCKS4: 205 alive / 150 gold
- SOCKS5: 191 alive / 139 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25618
- Ever gold: 1069

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
