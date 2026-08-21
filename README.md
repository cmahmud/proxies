# SyndProxy private pool

## Current pool

- Alive now: 792
- Gold now: 390
- HTTP: 237 alive / 82 gold
- HTTPS: 125 alive / 23 gold
- SOCKS4: 180 alive / 127 gold
- SOCKS5: 250 alive / 158 gold

## Historical pool

- Discovered: 157412
- Ever alive: 29689
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
