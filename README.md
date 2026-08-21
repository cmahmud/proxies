# SyndProxy private pool

## Current pool

- Alive now: 749
- Gold now: 399
- HTTP: 197 alive / 83 gold
- HTTPS: 108 alive / 16 gold
- SOCKS4: 220 alive / 149 gold
- SOCKS5: 224 alive / 151 gold

## Historical pool

- Discovered: 155786
- Ever alive: 29304
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
