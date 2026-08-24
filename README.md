# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 385
- HTTP: 115 alive / 54 gold
- HTTPS: 63 alive / 14 gold
- SOCKS4: 171 alive / 154 gold
- SOCKS5: 194 alive / 163 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33381
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
