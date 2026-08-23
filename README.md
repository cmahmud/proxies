# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 381
- HTTP: 86 alive / 57 gold
- HTTPS: 35 alive / 10 gold
- SOCKS4: 173 alive / 156 gold
- SOCKS5: 176 alive / 158 gold

## Historical pool

- Discovered: 174823
- Ever alive: 33103
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
