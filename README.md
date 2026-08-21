# SyndProxy private pool

## Current pool

- Alive now: 928
- Gold now: 398
- HTTP: 308 alive / 89 gold
- HTTPS: 170 alive / 20 gold
- SOCKS4: 199 alive / 129 gold
- SOCKS5: 251 alive / 160 gold

## Historical pool

- Discovered: 157412
- Ever alive: 29707
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
