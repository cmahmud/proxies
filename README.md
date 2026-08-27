# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 420
- HTTP: 118 alive / 75 gold
- HTTPS: 174 alive / 21 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40564
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
