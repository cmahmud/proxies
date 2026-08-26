# SyndProxy validated proxy pool

## Current pool

- Alive now: 660
- Gold now: 417
- HTTP: 150 alive / 79 gold
- HTTPS: 160 alive / 24 gold
- SOCKS4: 163 alive / 153 gold
- SOCKS5: 187 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40270
- Ever gold: 1309

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
