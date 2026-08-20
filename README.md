# SyndProxy private pool

## Current pool

- Alive now: 1599
- Gold now: 581
- HTTP: 629 alive / 194 gold
- HTTPS: 417 alive / 95 gold
- SOCKS4: 242 alive / 141 gold
- SOCKS5: 311 alive / 151 gold

## Historical pool

- Discovered: 136248
- Ever alive: 22739
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
