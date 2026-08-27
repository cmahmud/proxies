# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 417
- HTTP: 113 alive / 73 gold
- HTTPS: 160 alive / 17 gold
- SOCKS4: 187 alive / 163 gold
- SOCKS5: 183 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41199
- Ever gold: 1318

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
