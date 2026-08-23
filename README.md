# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 390
- HTTP: 142 alive / 62 gold
- HTTPS: 65 alive / 14 gold
- SOCKS4: 186 alive / 154 gold
- SOCKS5: 192 alive / 160 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33188
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
