# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 434
- HTTP: 119 alive / 87 gold
- HTTPS: 158 alive / 21 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 193 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42181
- Ever gold: 1353

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
