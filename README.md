# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 445
- HTTP: 127 alive / 87 gold
- HTTPS: 53 alive / 30 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43672
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
