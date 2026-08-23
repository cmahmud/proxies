# SyndProxy validated proxy pool

## Current pool

- Alive now: 445
- Gold now: 369
- HTTP: 67 alive / 48 gold
- HTTPS: 37 alive / 8 gold
- SOCKS4: 164 alive / 156 gold
- SOCKS5: 177 alive / 157 gold

## Historical pool

- Discovered: 173623
- Ever alive: 33019
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
