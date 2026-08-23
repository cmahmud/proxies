# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 392
- HTTP: 109 alive / 64 gold
- HTTPS: 55 alive / 14 gold
- SOCKS4: 170 alive / 152 gold
- SOCKS5: 184 alive / 162 gold

## Historical pool

- Discovered: 175447
- Ever alive: 33163
- Ever gold: 1228

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
