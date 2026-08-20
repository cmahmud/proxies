# SyndProxy private pool

## Current pool

- Alive now: 1586
- Gold now: 584
- HTTP: 575 alive / 194 gold
- HTTPS: 455 alive / 100 gold
- SOCKS4: 254 alive / 138 gold
- SOCKS5: 302 alive / 152 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23334
- Ever gold: 918

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
