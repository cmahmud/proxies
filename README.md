# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 437
- HTTP: 104 alive / 78 gold
- HTTPS: 55 alive / 26 gold
- SOCKS4: 185 alive / 163 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49140
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
