# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 384
- HTTP: 127 alive / 61 gold
- HTTPS: 39 alive / 16 gold
- SOCKS4: 172 alive / 152 gold
- SOCKS5: 177 alive / 155 gold

## Historical pool

- Discovered: 176557
- Ever alive: 33207
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
