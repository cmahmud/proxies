# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 387
- HTTP: 94 alive / 60 gold
- HTTPS: 44 alive / 14 gold
- SOCKS4: 163 alive / 154 gold
- SOCKS5: 178 alive / 159 gold

## Historical pool

- Discovered: 175389
- Ever alive: 33124
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
