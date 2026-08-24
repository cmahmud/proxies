# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 382
- HTTP: 137 alive / 68 gold
- HTTPS: 46 alive / 13 gold
- SOCKS4: 186 alive / 150 gold
- SOCKS5: 190 alive / 151 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33227
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
