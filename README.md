# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 402
- HTTP: 101 alive / 63 gold
- HTTPS: 179 alive / 16 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 191 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41056
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
