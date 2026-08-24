# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 438
- HTTP: 148 alive / 83 gold
- HTTPS: 88 alive / 22 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 187 alive / 172 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33979
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
