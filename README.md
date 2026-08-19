# SyndProxy private pool

## Current pool

- Alive now: 1049
- Gold now: 522
- HTTP: 376 alive / 160 gold
- HTTPS: 250 alive / 90 gold
- SOCKS4: 222 alive / 150 gold
- SOCKS5: 201 alive / 122 gold

## Historical pool

- Discovered: 123229
- Ever alive: 18998
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
