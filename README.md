# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 389
- HTTP: 118 alive / 70 gold
- HTTPS: 40 alive / 14 gold
- SOCKS4: 164 alive / 152 gold
- SOCKS5: 176 alive / 153 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33240
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
