# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 381
- HTTP: 104 alive / 57 gold
- HTTPS: 46 alive / 11 gold
- SOCKS4: 163 alive / 155 gold
- SOCKS5: 178 alive / 158 gold

## Historical pool

- Discovered: 175389
- Ever alive: 33124
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
