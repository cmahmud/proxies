# SyndProxy private pool

## Current pool

- Alive now: 988
- Gold now: 475
- HTTP: 320 alive / 136 gold
- HTTPS: 253 alive / 83 gold
- SOCKS4: 205 alive / 122 gold
- SOCKS5: 210 alive / 134 gold

## Historical pool

- Discovered: 117155
- Ever alive: 17571
- Ever gold: 686

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
