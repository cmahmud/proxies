# SyndProxy private pool

## Current pool

- Alive now: 817
- Gold now: 387
- HTTP: 257 alive / 78 gold
- HTTPS: 128 alive / 22 gold
- SOCKS4: 182 alive / 127 gold
- SOCKS5: 250 alive / 160 gold

## Historical pool

- Discovered: 157412
- Ever alive: 29694
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
