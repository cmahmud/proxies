# SyndProxy private pool

## Current pool

- Alive now: 777
- Gold now: 400
- HTTP: 205 alive / 75 gold
- HTTPS: 139 alive / 19 gold
- SOCKS4: 211 alive / 152 gold
- SOCKS5: 222 alive / 154 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25612
- Ever gold: 1069

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
