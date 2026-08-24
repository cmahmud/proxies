# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 380
- HTTP: 102 alive / 62 gold
- HTTPS: 48 alive / 13 gold
- SOCKS4: 159 alive / 152 gold
- SOCKS5: 169 alive / 153 gold

## Historical pool

- Discovered: 176240
- Ever alive: 33203
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
