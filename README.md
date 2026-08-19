# SyndProxy private pool

## Current pool

- Alive now: 901
- Gold now: 470
- HTTP: 278 alive / 122 gold
- HTTPS: 212 alive / 86 gold
- SOCKS4: 186 alive / 123 gold
- SOCKS5: 225 alive / 139 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17497
- Ever gold: 668

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
