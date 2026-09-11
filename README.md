# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 437
- HTTP: 99 alive / 78 gold
- HTTPS: 51 alive / 26 gold
- SOCKS4: 185 alive / 164 gold
- SOCKS5: 176 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49121
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
