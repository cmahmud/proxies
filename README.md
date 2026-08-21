# SyndProxy private pool

## Current pool

- Alive now: 961
- Gold now: 387
- HTTP: 335 alive / 78 gold
- HTTPS: 168 alive / 21 gold
- SOCKS4: 208 alive / 128 gold
- SOCKS5: 250 alive / 160 gold

## Historical pool

- Discovered: 157412
- Ever alive: 29703
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
