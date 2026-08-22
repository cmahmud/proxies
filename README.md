# SyndProxy private pool

## Current pool

- Alive now: 862
- Gold now: 402
- HTTP: 268 alive / 93 gold
- HTTPS: 177 alive / 29 gold
- SOCKS4: 200 alive / 141 gold
- SOCKS5: 217 alive / 139 gold

## Historical pool

- Discovered: 163262
- Ever alive: 31780
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
