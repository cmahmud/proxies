# SyndProxy validated proxy pool

## Current pool

- Alive now: 608
- Gold now: 414
- HTTP: 97 alive / 69 gold
- HTTPS: 151 alive / 20 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 187 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41298
- Ever gold: 1322

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
