# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 406
- HTTP: 111 alive / 65 gold
- HTTPS: 176 alive / 14 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41185
- Ever gold: 1318

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
