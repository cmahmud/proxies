# SyndProxy private pool

## Current pool

- Alive now: 983
- Gold now: 478
- HTTP: 315 alive / 137 gold
- HTTPS: 250 alive / 82 gold
- SOCKS4: 207 alive / 123 gold
- SOCKS5: 211 alive / 136 gold

## Historical pool

- Discovered: 117155
- Ever alive: 17571
- Ever gold: 686

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
