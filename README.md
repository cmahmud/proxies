# SyndProxy private pool

## Current pool

- Alive now: 735
- Gold now: 344
- HTTP: 196 alive / 72 gold
- HTTPS: 136 alive / 16 gold
- SOCKS4: 210 alive / 139 gold
- SOCKS5: 193 alive / 117 gold

## Historical pool

- Discovered: 145545
- Ever alive: 25366
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
