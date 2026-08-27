# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 411
- HTTP: 110 alive / 67 gold
- HTTPS: 174 alive / 16 gold
- SOCKS4: 183 alive / 163 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41186
- Ever gold: 1318

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
