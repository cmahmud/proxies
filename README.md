# SyndProxy private pool

## Current pool

- Alive now: 826
- Gold now: 386
- HTTP: 224 alive / 80 gold
- HTTPS: 155 alive / 22 gold
- SOCKS4: 212 alive / 141 gold
- SOCKS5: 235 alive / 143 gold

## Historical pool

- Discovered: 144768
- Ever alive: 25270
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
