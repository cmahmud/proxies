# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 437
- HTTP: 128 alive / 83 gold
- HTTPS: 96 alive / 23 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33993
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
