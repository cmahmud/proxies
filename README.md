# SyndProxy private pool

## Current pool

- Alive now: 918
- Gold now: 409
- HTTP: 288 alive / 98 gold
- HTTPS: 191 alive / 31 gold
- SOCKS4: 207 alive / 141 gold
- SOCKS5: 232 alive / 139 gold

## Historical pool

- Discovered: 163262
- Ever alive: 31780
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
