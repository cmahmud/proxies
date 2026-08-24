# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 375
- HTTP: 134 alive / 66 gold
- HTTPS: 51 alive / 14 gold
- SOCKS4: 172 alive / 147 gold
- SOCKS5: 176 alive / 148 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33221
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
