# SyndProxy private pool

## Current pool

- Alive now: 1718
- Gold now: 632
- HTTP: 614 alive / 226 gold
- HTTPS: 565 alive / 99 gold
- SOCKS4: 224 alive / 147 gold
- SOCKS5: 315 alive / 160 gold

## Historical pool

- Discovered: 142697
- Ever alive: 24323
- Ever gold: 982

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
