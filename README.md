# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 374
- HTTP: 145 alive / 68 gold
- HTTPS: 42 alive / 12 gold
- SOCKS4: 171 alive / 148 gold
- SOCKS5: 179 alive / 146 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33227
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
