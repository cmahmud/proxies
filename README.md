# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 440
- HTTP: 118 alive / 88 gold
- HTTPS: 146 alive / 22 gold
- SOCKS4: 184 alive / 161 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42185
- Ever gold: 1353

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
