# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 420
- HTTP: 108 alive / 75 gold
- HTTPS: 169 alive / 21 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 188 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40552
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
