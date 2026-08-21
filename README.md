# SyndProxy private pool

## Current pool

- Alive now: 841
- Gold now: 368
- HTTP: 260 alive / 73 gold
- HTTPS: 141 alive / 22 gold
- SOCKS4: 204 alive / 129 gold
- SOCKS5: 236 alive / 144 gold

## Historical pool

- Discovered: 157406
- Ever alive: 29665
- Ever gold: 1134

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
