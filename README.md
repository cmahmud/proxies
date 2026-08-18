# SyndProxy private pool

## Current pool

- Alive now: 807
- Gold now: 211
- HTTP: 240 alive / 25 gold
- HTTPS: 138 alive / 8 gold
- SOCKS4: 203 alive / 96 gold
- SOCKS5: 226 alive / 82 gold

## Historical pool

- Discovered: 91700
- Ever alive: 8643
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
