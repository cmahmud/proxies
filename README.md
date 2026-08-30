# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 430
- HTTP: 106 alive / 74 gold
- HTTPS: 48 alive / 26 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 190 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44447
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
