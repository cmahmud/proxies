# SyndProxy private pool

## Current pool

- Alive now: 819
- Gold now: 419
- HTTP: 212 alive / 91 gold
- HTTPS: 169 alive / 28 gold
- SOCKS4: 217 alive / 139 gold
- SOCKS5: 221 alive / 161 gold

## Historical pool

- Discovered: 151684
- Ever alive: 27709
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
