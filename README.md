# SyndProxy private pool

## Current pool

- Alive now: 1616
- Gold now: 585
- HTTP: 590 alive / 195 gold
- HTTPS: 479 alive / 99 gold
- SOCKS4: 241 alive / 141 gold
- SOCKS5: 306 alive / 150 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23363
- Ever gold: 918

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
