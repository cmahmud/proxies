# SyndProxy private pool

## Current pool

- Alive now: 1055
- Gold now: 380
- HTTP: 359 alive / 92 gold
- HTTPS: 275 alive / 28 gold
- SOCKS4: 188 alive / 121 gold
- SOCKS5: 233 alive / 139 gold

## Historical pool

- Discovered: 153749
- Ever alive: 28828
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
