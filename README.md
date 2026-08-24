# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 376
- HTTP: 151 alive / 68 gold
- HTTPS: 37 alive / 13 gold
- SOCKS4: 181 alive / 148 gold
- SOCKS5: 183 alive / 147 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33227
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
