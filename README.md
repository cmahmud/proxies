# SyndProxy private pool

## Current pool

- Alive now: 973
- Gold now: 477
- HTTP: 314 alive / 137 gold
- HTTPS: 250 alive / 83 gold
- SOCKS4: 203 alive / 122 gold
- SOCKS5: 206 alive / 135 gold

## Historical pool

- Discovered: 117155
- Ever alive: 17571
- Ever gold: 686

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
