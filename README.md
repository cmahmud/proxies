# SyndProxy private pool

## Current pool

- Alive now: 722
- Gold now: 382
- HTTP: 155 alive / 74 gold
- HTTPS: 158 alive / 21 gold
- SOCKS4: 200 alive / 139 gold
- SOCKS5: 209 alive / 148 gold

## Historical pool

- Discovered: 145568
- Ever alive: 25510
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
