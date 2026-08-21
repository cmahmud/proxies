# SyndProxy private pool

## Current pool

- Alive now: 818
- Gold now: 384
- HTTP: 253 alive / 76 gold
- HTTPS: 132 alive / 21 gold
- SOCKS4: 183 alive / 127 gold
- SOCKS5: 250 alive / 160 gold

## Historical pool

- Discovered: 157412
- Ever alive: 29696
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
