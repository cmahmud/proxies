# SyndProxy private pool

## Current pool

- Alive now: 905
- Gold now: 403
- HTTP: 244 alive / 93 gold
- HTTPS: 192 alive / 23 gold
- SOCKS4: 205 alive / 133 gold
- SOCKS5: 264 alive / 154 gold

## Historical pool

- Discovered: 154717
- Ever alive: 29028
- Ever gold: 1119

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
