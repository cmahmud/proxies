# SyndProxy validated proxy pool

## Current pool

- Alive now: 617
- Gold now: 411
- HTTP: 107 alive / 65 gold
- HTTPS: 151 alive / 17 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 183 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41218
- Ever gold: 1318

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
